import requests
from components.tabs.dto.tab_dto import TabDTO
from enums.api.ApiEnum import GamesApi
from enums.games.TcgEnum import *
from services.ConfigService import ConfigService
from services.MainTabService import MainTabService

class CreateEditTabModel():
    
    def __init__(self, create_edit_tab_service) -> None:
        self.main_tab_service = MainTabService()
        self.config_service = ConfigService()
        self.create_edit_tab_service = create_edit_tab_service
        self.total_exp_list = self.get_expansions()

    def set_controller(self, controller) -> None:
        self.controller = controller
        
    def add_new_tab(self, tab_dto: TabDTO) -> None:
        self.main_tab_service.add_new_tab(tab_dto)
        
    def cancel_procedure(self) -> None:
        self.create_edit_tab_service.destroy_modal_components()

    def get_expansions_by_tcg(self, choice: str) -> None:
        self.specific_exp_list = []
        match choice:
            case MtgGenerics.display_name.value:
                for exp in self.total_exp_list:
                    if exp["game_id"] == MtgGenerics.id.value:
                        self.specific_exp_list.append(exp["name"])
                self.controller.set_expansions_by_tcg(self.specific_exp_list)

            case PkmGenerics.display_name.value:
                for exp in self.total_exp_list:
                    if exp["game_id"] == PkmGenerics.id.value:
                        self.specific_exp_list.append(exp["name"])
                self.controller.set_expansions_by_tcg(self.specific_exp_list)        
                
    def get_expansions(self) -> list:
        headers = {
            'Authorization': f'Bearer {self.config_service.get_auth_token()}'
        }
        
        try:
            return requests.get(f'{GamesApi.GET_ALL_EXPANSIONS.value}', headers=headers).json()
        except Exception as e:
            # to change with a modal
            print(f"An error occurred while getting all expansions, error is: {e}")

