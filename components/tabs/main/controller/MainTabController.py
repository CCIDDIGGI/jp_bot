from customtkinter import *
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
            self.view.set_parent()
            self.model.set_controller(self)
            MainTabService(self._instance)
            
            # initialized
            self._initialized = True

    def set_parent(self, parent) -> None:
        self.model.set_parent(parent)

    def add_new_tab(self, tab_dto: TabDTO) -> None:
        self.view.render_new_tab(tab_dto)
        
    def pass_tab_widget_to_controller(self, tab_widget: CTkFrame, tab_dto: TabDTO) -> None:
        self.model.initialize_generic_tab(tab_widget, tab_dto)
        
    def delete_tab(self, tab_name: str) -> None:
        self.view.delete_tab(tab_name)
        
    def edit_tab(self, tab_dto: TabDTO) -> None:
        self.model.edit_tab(tab_dto)
        