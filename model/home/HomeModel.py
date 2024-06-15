
import requests
from enums.api.ApiEnum import BearerToken, GamesApi
from enums.games.pkm.pkmEnum import PkmGenerics


class HomeModel():
    
    def __init__(self) -> None:
        self.get_expansions()
    
    def get_expansions(self) -> list:
                
        headers = {
            'Authorization': f'Bearer {BearerToken.TOKEN.value}'
        }
        
        exp_dict = requests.get(f'{GamesApi.GET_ALL_EXPANSIONS.value}', headers=headers).json()
        exp_list = []
        for x in range(len(exp_dict) -1):
            if exp_dict[x]["game_id"] == PkmGenerics.game_id.value:
                exp_list.append(exp_dict[x]["name"])
                
        return exp_list
           
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
