from typing import Self
from customtkinter import *

from components.tabs.dto.tab_dto import TabDTO
from components.tabs.generic.view.GenericTabView import GenericTabView

class MainTabView(CTkTabview):
    _instance = None
    
    def __new__(cls, *args, **kwargs) -> Self:
        if cls._instance is None:
            cls._instance = super(MainTabView, cls).__new__(cls)
        return cls._instance
    
    # child of MainView -> parent argument is MainView
    def __init__(self, parent):
        
        # main setup
        if not hasattr(self, '_initialized') or not self._initialized:
            super().__init__(parent)
            self.configure(fg_color = "green")
            self.parent = parent
            self.grid(row=1, column=1, columnspan=2, sticky='nsew')
            
            # initialized
            self._initialized = True
            
    def set_controller(self, controller) -> None:
        self.controller = controller
    
    def add_new_tab(self, tab_dto: TabDTO) -> None:
        self.add(tab_dto.name)
        tab_widget = self.tab(tab_dto.name)
        GenericTabView(tab_widget)
        print("added")