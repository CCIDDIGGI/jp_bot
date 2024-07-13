
import aiohttp
import requests
from enums.api.ApiEnum import BearerToken, CartApi, GamesApi
from enums.games.mtg.mtgEnum import MtgGenerics

class HomeModel():
    mtg_exp_dict = list
    # used for ui objects like comboboxes
    mtg_exp_list = list

    diff_value = int
    # initialized as 1 in case the user does not trigger the method in the view even once
    diff_type = 1
    maximum_threshold = 0
    support_threshold_var = 0
        
    def __init__(self) -> None:
        self.get_expansions()
        
    def get_mtg_exp_dict(self) -> dict:
        return self.mtg_exp_dict

    def set_mtg_exp_dict(self, value) -> None:
        if not value:
            raise ValueError("The MTG expansions dictionary list cannot be empty!")
        
        self.mtg_exp_dict = value

    def get_mtg_exp_list(self) -> list:
        return self.mtg_exp_list

    def set_mtg_exp_list(self, value) -> None:
        if not value:
            raise ValueError("The MTG expansions list cannot be empty!")
        
        self.mtg_exp_list = value

    # probably going to be replaced by a service
    def set_diff_type(self, diff_type: int) -> None:
        self.diff_type = diff_type
        print(f'printed from model, type is {self.diff_type}')

    # probably going to be replaced by a service
    def set_diff_value(self, diff_value: int) -> None:
        self.diff_value = diff_value
        print(f'printed from model, value is {self.diff_value}')

    # probably going to be replaced by a service
    def set_maximum_threshold_value(self, maximum_threshold_value: int) -> None:
        # converting from eur to cents
        self.maximum_threshold = maximum_threshold_value * 100
        self.support_threshold_var = self.maximum_threshold
        print(f'printed from model, threshold max value is {self.maximum_threshold}')

    # gets all the mtg expansions
    def get_expansions(self) -> None:
                
        headers = {
            'Authorization': f'Bearer {BearerToken.TOKEN.value}'
        }
        
        # exp_dict is now list of dictionaries
        exp_dict = requests.get(f'{GamesApi.GET_ALL_EXPANSIONS.value}', headers=headers).json()
        self.set_mtg_exp_dict(exp_dict)

        exp_list = []
        for x in range(len(exp_dict) -1):
            if exp_dict[x]["game_id"] == MtgGenerics.id.value:
                exp_list.append(exp_dict[x]["name"])
                
        self.set_mtg_exp_list(exp_list)
        
    def get_exp_id_by_exp_name(self, exp_name: str) -> int:
        for x in range(len(self.mtg_exp_dict) -1):
            if self.mtg_exp_dict[x]["name"] == exp_name:
                return self.mtg_exp_dict[x]["id"]
        return 0
                
    
    async def get_listings_by_exp_id(self, exp_id) -> None:
        listings = object

        headers = {
            'Authorization': f'Bearer {BearerToken.TOKEN.value}'
        }
        
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(f'{GamesApi.GET_LISTING_BY_EXPANSION_ID.value}{exp_id}', headers=headers) as response:
                    response.raise_for_status()
                    listings = await response.json() 
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
                print(f"Something went wrong while fetching all the listing by expansion id: {exp_id}, error is {e}")
                return
        
        # data analisys
        # loop through every key in list
        for key, value in listings.items():
            # if key == "279435":
                # loop through every single listing for the specific key (blueprint_id)
                items_to_compare = []
                for item in value:
                    # create list to store values to compare
                    listing_blueprint_id = item.get("properties_hash", {})
                    if all([
                        listing_blueprint_id.get("condition") == "Near Mint",
                        listing_blueprint_id.get("mtg_language") == "it",
                        item.get("user", {}).get("can_sell_via_hub") == True,
                    ]):
                        # main logic
                        # set first item for each key
                        if  len(items_to_compare) == 0:
                            items_to_compare.append(item)

                        # if the first item is already fetched, compare the current item with the first
                        else:

                            # check if the i-th item has a price different from the first item
                            if item["price_cents"] != items_to_compare[0]["price_cents"]:
                                # check difference type (percentage or flat value)
                                # percentage
                                if self.diff_type == 1:
                                    if (item["price_cents"] - ((self.diff_value / 100) * item["price_cents"])) > items_to_compare[0]["price_cents"]:
                                        # add item to cart
                                        print(items_to_compare[0]["blueprint_id"])
                                        print(f"{items_to_compare[0]["name_en"]}, listed for: {items_to_compare[0]["price_cents"]} by: {items_to_compare[0]['user']["username"]} is at least {self.diff_value} % cheaper then {item["price_cents"]}  by: {item['user']["username"]} , adding it to cart...")
                                        await self.add_item_to_cart(items_to_compare[0]["id"])
                                        
                                        # check if maximum threshold is set
                                        if self.maximum_threshold > 0:
                                            self.support_threshold_var -= items_to_compare[0]["price_cents"]
                                            if self.support_threshold_var <= 0:
                                                print("Maximum price threshold exceeded, exiting...")
                                                return
                                        # remove break if you want to get multiple cards
                                        break
                




    async def add_item_to_cart(self, id: int) -> None:
        headers = {
            'Authorization': f'Bearer {BearerToken.TOKEN.value}'
        }

        payload = {
            "product_id": id,
            "quantity": 1,
            "via_cardtrader_zero": True,
            "billing_address": {
                "name": "name surname",
                "street": "via del bulo 00",
                "zip": "50143",
                "city": "firenze",
                "state_or_province": "FI",
                "country_code": "IT",
                "phone": "123456789"
            },
            "shipping_address": {
                "name": "name surname",
                "street": "via del bulo 00",
                "zip": "50143",
                "city": "firenze",
                "state_or_province": "FI",
                "country_code": "IT"
            }
        }

        response = requests.post(CartApi.ADD_PRODUCT_TO_CART.value, json=payload, headers=headers)

        if response.status_code == 200:
            print("SUCCESS")
        else:
            print(response.status_code, response.text)
    
        
       
