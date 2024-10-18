import aiohttp
from components.tabs.dto.tab_dto import TabDTO
from enums.api.ApiEnum import GamesApi
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
                    print(listings)
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