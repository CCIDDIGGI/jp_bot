
from typing import Self

from components.tabs.dto.tab_dto import TabDTO
from services.MainTabService import MainTabService

class MainTabController():
    _instance = None
    
    def __new__(cls, *args, **kwargs) -> Self:
        if cls._instance is None:
            cls._instance = super(MainTabController, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, model, view) -> None:
        if not hasattr(self, '_initialized') or not self._initialized:
            self.model = model
            self.view = view
            self.view.set_controller(self)
            self.model.set_controller(self)
            MainTabService(self._instance)
            
            # initialized
            self._initialized = True

    def add_new_tab(self, tab_dto: TabDTO) -> None:
        self.view.add_new_tab(tab_dto)