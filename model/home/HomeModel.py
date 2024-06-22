
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
        # insert all possible http error exceptions
        except:
            print(f"Something went wrong while fetching all the listing by expansion id: {exp_id}")
            return
        
        for x in listings.keys():
            for y in range(len(listings[x]) -1):
                if "properties_hash" in listings[x][y]:
                    if "condition" in listings[x][y]["properties_hash"]:
                        if listings[x][y]["properties_hash"]["condition"] == "Near Mint":
                            print(listings[x][y])
       

    
        
           
    def test_api(self):
        test = object

        headers = {
            'Authorization': f'Bearer {BearerToken.TOKEN.value}'
        }

        # return type is dict
        test = requests.get(f'{GamesApi.GET_LISTING_BY_EXPANSION_ID.value}3403', headers=headers).json()

        test_list = test["261058"]

        print(test_list[0])
        print(test_list[-1])
