
import aiohttp
import asyncio
import requests
from threading import Event, Thread
from enums.api.ApiEnum import BearerToken, CartApi, GamesApi
from enums.games.mtg.mtgEnum import MtgGenerics
from services.ConfigService import ConfigService

class HomeModel():
    mtg_exp_dict = list
    # used for ui objects like comboboxes
    mtg_exp_list = list

    # probably to initialize this
    diff_value = int
    # initialized as 1 in case the user does not trigger the method in the view even once
    diff_type = 1
    maximum_threshold = 0
    support_threshold_var = 0
    exp_id = 0

    stop_event = Event()
    fetch_thread = None
        
    def __init__(self) -> None:
        self.config_service = ConfigService()
        self.get_expansions()

    def set_controller(self, controller) -> None:
        self.controller = controller
        
    def assign_default_values(self,  default_diff_value: int, default_max_threshold_value: int) -> None:
        self.diff_value = default_diff_value
        self.maximum_threshold = default_max_threshold_value * 100
        self.support_threshold_var = self.maximum_threshold
        
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
    
    def set_listings_exp_id(self, value: int) -> None:
        if not value:
            raise ValueError("expansion list id cannot be empty")
        self.exp_id = value

    # probably going to be replaced by a service
    def set_diff_type(self, diff_type: int) -> None:
        self.diff_type = diff_type

    # probably going to be replaced by a service
    def set_diff_value(self, diff_value: int) -> None:
        self.diff_value = diff_value

    # probably going to be replaced by a service
    def set_maximum_threshold_value(self, maximum_threshold_value: int) -> None:
        # converting from eur to cents
        self.maximum_threshold = maximum_threshold_value * 100
        self.support_threshold_var = self.maximum_threshold

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
        
    def set_exp_id_by_exp_name(self, exp_name: str) -> None:
        for x in range(len(self.mtg_exp_dict) -1):
            if self.mtg_exp_dict[x]["name"] == exp_name:
                return self.set_listings_exp_id(self.mtg_exp_dict[x]["id"])

                
    
    async def get_listings_by_exp_id(self, exp_id, process_callback) -> None:
        headers = {
            'Authorization': f'Bearer {BearerToken.TOKEN.value}',
            'Cache-Control': 'no-cache, no-store, must-revalidate',
            'Pragma': 'no-cache',
            'Expires': '0'
        }
        
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(f'{GamesApi.GET_LISTING_BY_EXPANSION_ID.value}{exp_id}', headers=headers) as response:
                    response.raise_for_status()
                    listings = await response.json() 
                    if self.stop_event.is_set():
                        return
                    await process_callback(listings)
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
    
    async def process_listings(self, listings) -> None:
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
                                    self.controller.send_info_to_view(f"{items_to_compare[0]["name_en"]}, listed for: {items_to_compare[0]["price_cents"]} by: {items_to_compare[0]['user']["username"]} is at least {self.diff_value} % cheaper then {item["price_cents"]}  by: {item['user']["username"]} , adding it to cart...")
                                    await self.add_item_to_cart(items_to_compare[0]["id"])
                                    
                                    # check if maximum threshold is set
                                    if self.maximum_threshold > 0:
                                        self.support_threshold_var -= items_to_compare[0]["price_cents"]
                                        if self.support_threshold_var <= 0:
                                            self.controller.send_info_to_view("Maximum price threshold exceeded, exiting...")
                                            self.controller.change_btn_configuration()
                                            self.stop_fetch()
                                            return
                                    # remove break if you want to get multiple cards
                                    break
                            # flat value
                            if self.diff_type == 2:
                                if items_to_compare[0]["price_cents"] < (item["price_cents"] - (self.diff_value * 100)):
                                    # add item to cart
                                    self.controller.send_info_to_view(f"{items_to_compare[0]["name_en"]}, listed for: {items_to_compare[0]["price_cents"]} by: {items_to_compare[0]['user']["username"]} is at least {self.diff_value}€ cheaper then {item["price_cents"]}  by: {item['user']["username"]} , adding it to cart...")
                                    await self.add_item_to_cart(items_to_compare[0]["id"])
                                    
                                    # check if maximum threshold is set
                                    if self.maximum_threshold > 0:
                                        self.support_threshold_var -= items_to_compare[0]["price_cents"]
                                        if self.support_threshold_var <= 0:
                                            self.controller.send_info_to_view("Maximum price threshold exceeded, exiting...")
                                            self.controller.change_btn_configuration()
                                            self.stop_fetch()
                                            return
                                    # remove break if you want to get multiple cards
                                    break

                if self.stop_event.is_set():
                    return
                




    async def add_item_to_cart(self, id: int) -> None:
        print(self.config_service.config)
        headers = {
            'Authorization': f'Bearer {self.config_service.config["Auth token"]}'
        }

        payload = {
            "product_id": id,
            "quantity": 1,
            "via_cardtrader_zero": True,
            "billing_address": {
                "name": self.config_service.config["Billing address name"],
                "street": self.config_service.config["Billing Street"],
                "zip": self.config_service.config["Billing zip"],
                "city": self.config_service.config["Billing city"],
                "state_or_province": self.config_service.config["Billing state or province"],
                "country_code": self.config_service.config["Billing country code"],
                "phone": self.config_service.config["Billing phone"]
            },
            "shipping_address": {
                "name": self.config_service.config["Shipping name"],
                "street": self.config_service.config["Shipping street"],
                "zip": self.config_service.config["Shipping zip"],
                "city": self.config_service.config["Shipping city"],
                "state_or_province": self.config_service.config["Shipping state or province"],
                "country_code": self.config_service.config["Shipping country code"]
            }
        }

        response = requests.post(CartApi.ADD_PRODUCT_TO_CART.value, json=payload, headers=headers)

        if response.status_code == 200:
            self.controller.send_info_to_view("Item succesfully added to cart!")
        else:
            self.controller.send_info_to_view(f"An error occurred while addding the item to cart: {response.text}")

    def start_fetch(self) -> None:
        self.stop_event.clear()
        self.fetch_thread = Thread(target=self.run_async_task, args=(self.get_listings_by_exp_id(self.exp_id, self.process_listings),))
        self.fetch_thread.start()

    def stop_fetch(self) -> None:
        self.stop_event.set()
        if self.fetch_thread and self.fetch_thread.is_alive():
            self.fetch_thread.join()
        self.support_threshold_var = self.maximum_threshold

       
    def run_async_task(self, coro):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(coro)
        loop.close()