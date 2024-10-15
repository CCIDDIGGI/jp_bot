from customtkinter import *
from typing import Self
from components.tabs.dto.tab_dto import TabDTO
from components.tabs.generic.controller.GenericTabController import GenericTabController
from components.tabs.generic.model.GenericTabModel import GenericTabModel
from components.tabs.generic.view.GenericTabView import GenericTabView
from services.CreateEditTabService import CreateEditTabService

class MainTabModel():

    _instance = None
    # a list of all the child tabs created
    generic_tabs = []
    
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
    
    def check_tab_id(self, tab_dto: TabDTO) -> bool:
        # base case, generic tab list has at least one tab
        if len(self.generic_tabs) > 0:
            for index, tab in enumerate(self.generic_tabs):
                if tab.id == tab_dto.id:
                    self.generic_tabs[index] = tab_dto
                    return True        
        self.generic_tabs.append(tab_dto)
        return False
        
            
    def initialize_generic_tab(self, tab_widget: CTkFrame, tab_dto: TabDTO) -> None:
        GenericTabController(GenericTabModel(), GenericTabView(tab_widget), tab_dto)
        
    def edit_tab(self, tab_dto: TabDTO) -> None:
        self.create_edit_tab_service.create_modal_components(self.parent, tab_dto)
        
    def initialize_edited_tab(self, tab_dto: TabDTO) -> None:
        print("edited")
        for instance in GenericTabController.instances:
            if instance.tab_dto.id == tab_dto.id:
                # rename tab
                self.controller.rename_tab(instance.tab_dto.name, tab_dto.name)
                # re-initialize instance tab_dto and redraw tab
                instance.tab_dto = tab_dto
                instance.redraw_tab()
                        
    def delete_tab(self, tab_dto_id: str) -> None:
        # generic tab should always have at least one item here
        for tab in self.generic_tabs:
            if tab.id == tab_dto_id:
                self.generic_tabs.remove(tab)
                return    