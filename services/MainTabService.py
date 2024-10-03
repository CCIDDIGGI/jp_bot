
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
                
    def add_new_tab(self, tab_dto: TabDTO) -> None:
        self.main_tab_controller.add_new_tab(tab_dto)
        