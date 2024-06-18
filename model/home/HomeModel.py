
import requests
from enums.api.ApiEnum import BearerToken, GamesApi
from enums.games.mtg.mtgEnum import MtgGenerics


class HomeModel():
    mtg_exp_dict = dict
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
        
        exp_dict = requests.get(f'{GamesApi.GET_ALL_EXPANSIONS.value}', headers=headers).json()
        self.set_mtg_exp_dict(exp_dict)

        exp_list = []
        for x in range(len(exp_dict) -1):
            if exp_dict[x]["game_id"] == MtgGenerics.id.value:
                exp_list.append(exp_dict[x]["name"])
                
        self.set_mtg_exp_list(exp_list)
        
           
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
