import aiohttp
import requests
from components.tabs.dto.tab_dto import TabDTO
from enums.api.ApiEnum import CartApi, GamesApi
from services.ConfigService import ConfigService
from services.MainTabService import MainTabService

class GenericTabModel():
    headers = {}
    
    def __init__(self) -> None:
        self.main_tab_service = MainTabService()
        self.config_service = ConfigService()
        self.init_headers()
        
    def init_headers(self) -> None:
        self.headers = {
            'Authorization': f'Bearer {self.config_service.get_auth_token()}'      
        }
    
    def set_controller(self, controller) -> None:
        self.controller = controller
        
    def delete_tab(self, tab_dto: TabDTO) -> None:
        self.main_tab_service.delete_tab(tab_dto)    
        
    def edit_tab(self, tab_dto: TabDTO) -> None:
        self.main_tab_service.edit_tab(tab_dto)
                
    async def start_process(self, tab_dto: TabDTO) -> None:
        # get listings by exp id
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(f'{GamesApi.GET_LISTING_BY_EXPANSION_ID.value}{tab_dto.exp_id}', headers=self.headers) as response:
                    response.raise_for_status()
                    listings = await response.json() 
                    await self.process_listings_items(listings.items(), tab_dto)
            except aiohttp.ClientConnectionError as cce:
                print(f"A connection error occurred: {cce}")
                return
            # except requests.exceptions.ConnectTimeout as cto:
            #     print(f"The request timed out while trying to connect to the remote server: {cto}")
            #     return
            except aiohttp.ClientResponseError as cre:
                print(f"Client response error: {cre}")
                return
            except Exception as e:
                print(f"Something went wrong while fetching all the listing by expansion id: {tab_dto.exp_id}, error is {e}")
                return
            
    async def process_listings_items(self, listings, tab_dto: TabDTO) -> None:
        property_hash_for_language: str = None
        match tab_dto.tcg:
            case "Pokémon":
                property_hash_for_language = "pokemon_language"
            case "Magic: the Gathering":
                property_hash_for_language = "mtg_language"
        # loop throught every item found in listings
        for key, value in listings:
            
            first_listing = None
            for current_listing in value:
                if all([
                    current_listing.get("properties_hash", {}).get(property_hash_for_language) == "it",
                    current_listing.get("user", {}).get("can_sell_via_hub") == True
                ]):
                    # initialize first_listing if None 
                    if first_listing is None:
                        # check if current_listing condition is valid
                        if current_listing.get("properties_hash", {}).get("condition") in tab_dto.condition_comparison: 
                            first_listing = current_listing
    
                    # if first_listing is initialized, start main comparison logic    
                    else:
                        # check difference type
                        if tab_dto.price_difference_type == 1:
                            if current_listing.get("properties_hash", {}).get("condition") in tab_dto.condition_comparison[first_listing.get("properties_hash", {}).get("condition")]:
                                if (current_listing["price_cents"] - ((tab_dto.price_difference / 100) * current_listing["price_cents"])) > first_listing["price_cents"]:
                                    print(f"{first_listing['name_en']}, listed for: {first_listing['price_cents']} by: {first_listing['user']['username']} with id {first_listing["id"]} is at least {tab_dto.price_difference} % cheaper then {current_listing['price_cents']}  by: {current_listing['user']['username']} , adding it to cart...")
                                    await self.add_item_to_cart(first_listing["id"])
                                    break
                        # else:
                            
                        
                        
                
    async def add_item_to_cart(self, id: int) -> None:    
        payload = {
            "product_id": id,
            "quantity": 1,
            "via_cardtrader_zero": True,
        }

        response = requests.post(CartApi.ADD_PRODUCT_TO_CART.value, json=payload, headers=self.headers)
        
        if response.status_code == 200:
            print("Item succesfully added to cart!")
        else:
           print(f"An error occurred while addding the item to cart: {response.text}")
            