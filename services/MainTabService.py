
from typing import Self
from components.tabs.dto.tab_dto import TabDTO

class MainTabService():
    _instance = None
    
    def __new__(cls, *args, **kwargs) -> Self:
        if cls._instance is None:
            cls._instance = super(MainTabService, cls).__new__(cls)
        return cls._instance

    def __init__(self, *args) -> None:
        if args:
            if not hasattr(self, '_initialized') or not self._initialized:
                self.main_tab_controller = args[0]
                # initialized
                self._initialized = True
                
    def add_edit_tab(self, tab_dto: TabDTO) -> None:
        self.main_tab_controller.add_edit_tab(tab_dto)
        
    def delete_tab(self, tab_dto: TabDTO) -> None:
        self.main_tab_controller.delete_tab(tab_dto)
        
    def edit_tab(self, tab_dto: TabDTO) -> None:
        self.main_tab_controller.edit_tab(tab_dto)
        
    def check_duplicate_tab_names(self, tab_name: str, is_edit: bool) -> None:
        self.main_tab_controller.check_duplicate_tab_names(tab_name, is_edit)

        