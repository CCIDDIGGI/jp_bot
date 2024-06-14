
import requests
from enums.api.ApiEnum import BearerToken, GamesApi


class HomeModel():
    
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
