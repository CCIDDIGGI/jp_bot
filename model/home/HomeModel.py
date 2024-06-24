
import requests
from enums.api.ApiEnum import BearerToken, GamesApi
from enums.games.mtg.mtgEnum import MtgGenerics

class HomeModel():
    mtg_exp_dict = list
    # used for ui objects like comboboxes
    mtg_exp_list = list
    
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
                
    
    def get_listings_by_exp_id(self, exp_id) -> None:
        listings = object

        headers = {
            'Authorization': f'Bearer {BearerToken.TOKEN.value}'
        }
        
        try:
             listings = requests.get(f'{GamesApi.GET_LISTING_BY_EXPANSION_ID.value}{exp_id}', headers=headers).json()
        except requests.exceptions.ConnectionError as cer:
            print(f"A connection error occurred: {cer}")
            return
        # except requests.exceptions.ConnectTimeout as cto:
        #     print(f"The request timed out while trying to connect to the remote server: {cto}")
        #     return
        except requests.exceptions.HTTPError as httperr:
            print(f"An HTTP error occurred: {httperr}")
            return
        except:
            print(f"Something went wrong while fetching all the listing by expansion id: {exp_id}")
            return
        
        # data analisys
        for key, value in listings.items():
            if key == "279435":
                for item in value:
                    listing_blueprint_id = item.get("properties_hash", {})
                    if all([
                        listing_blueprint_id.get("condition") == "Near Mint",
                        listing_blueprint_id.get("mtg_language") == "it",
                        item.get("user", {}).get("can_sell_via_hub") == True,
                    ]):
                        self.compare_listings(item)
        
        # for x in listings.keys():
        #     if x == '279435':
        #         for y in range(len(listings[x]) -1):
        #             if "properties_hash" in listings[x][y]:
        #                 if "condition" in listings[x][y]["properties_hash"]:
        #                     if listings[x][y]["properties_hash"]["condition"] == "Near Mint":
        #                         if listings[x][y]["properties_hash"]["mtg_language"] == "it":
        #                             if listings[x][y]["user"]["can_sell_via_hub"] == True:
        #                                 print(listings[x][y])

    def compare_listings(self, listings: object) -> None:
        print(listings)
        
       
