from components.tabs.dto.tab_dto import TabDTO
from services.MainTabService import MainTabService

class GenericTabModel():
    
    def __init__(self) -> None:
        self.main_tab_service = MainTabService()
    
    def set_controller(self, controller) -> None:
        self.controller = controller
        
    def delete_tab(self, tab_name: str) -> None:
        self.main_tab_service.delete_tab(tab_name)    
        
    def edit_tab(self, tab_dto: TabDTO) -> None:
        self.main_tab_service.edit_tab(tab_dto)