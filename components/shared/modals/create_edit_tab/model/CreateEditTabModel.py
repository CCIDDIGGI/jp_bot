from services.MainTabService import MainTabService

class CreateEditTabModel():
    
    def __init__(self) -> None:
        self.main_tab_service = MainTabService()
        
    def add_new_tab(self) -> None:
        self.main_tab_service.add_new_tab()
        