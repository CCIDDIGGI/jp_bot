import requests
from typing import Self
from enums.api.ApiEnum import InfoApi
from services.ConfigService import ConfigService

class HeaderService():
    _instance = None
    username = ''
    
    def __new__(cls, *args, **kwargs) -> Self:
        if cls._instance is None:
            cls._instance = super(HeaderService, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self) -> None:
        self.config_service = ConfigService()

    def set_username(self, value: str) -> None:
        if not value:
            raise ValueError("Username cannot be empty!")
        self.username = value[:value.index('App')]

    def get_username(self) -> str:
        return self.username
        
    def fetch_username(self) -> None:
        headers = {
            'Authorization': f'Bearer {self.config_service.get_auth_token()}',
        }     
        
        try:
            response = requests.get(f'{InfoApi.GET_INFO.value}', headers=headers)
            user_data = response.json()
            self.set_username(user_data['name'])
            
        except ConnectionError as cer:
            print(f"A connection error occurred while fetching user informations: {cer}")
        except Exception as e:
            print(f"An unhandled error occurred while fetching user informations: {e}")