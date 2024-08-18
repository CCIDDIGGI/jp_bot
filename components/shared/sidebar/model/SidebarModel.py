
from services.MainTabService import MainTabService


class SidebarModel():
    
    def __init__(self) -> None:
        self.main_tab_service = MainTabService()
        
    def add(self) -> None:
        self.main_tab_service.add()