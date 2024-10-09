from customtkinter import *
from typing import Self
from components.tabs.dto.tab_dto import TabDTO
from components.tabs.generic.controller.GenericTabController import GenericTabController
from components.tabs.generic.model.GenericTabModel import GenericTabModel
from components.tabs.generic.view.GenericTabView import GenericTabView
from services.CreateEditTabService import CreateEditTabService

class MainTabModel():

    _instance = None
    
    def __new__(cls, *args, **kwargs) -> Self:
        if cls._instance is None:
            cls._instance = super(MainTabModel, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self) -> None:
        self.parent = None
        self.create_edit_tab_service = CreateEditTabService()

        
    def set_parent(self, parent) -> None:
        self.parent = parent
    
    def set_controller(self, controller) -> None:
        self.controller = controller
    
    def add_new_tab(self, tab_dto) -> None:
        pass

    def initialize_generic_tab(self, tab_widget: CTkFrame, tab_dto: TabDTO) -> None:
        GenericTabController(GenericTabModel(), GenericTabView(tab_widget), tab_dto)
        
    def edit_tab(self, tab_dto: TabDTO) -> None:
        self.create_edit_tab_service.create_modal_components(self.parent, tab_dto)
    