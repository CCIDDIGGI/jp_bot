from typing import Self
from customtkinter import *

from components.tabs.dto.tab_dto import TabDTO

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
        
    def set_parent(self) -> None:
        self.controller.set_parent(self.parent)
    
    def render_new_tab(self, tab_dto: TabDTO) -> None:
        self.add(tab_dto.name)
        tab_widget = self.tab(tab_dto.name)
        self.controller.pass_tab_widget_to_controller(tab_widget, tab_dto)
        # GenericTabView(tab_widget)

    def delete_tab(self, tab_name: str) -> None:
        self.delete(tab_name)
        
    def rename_tab(self, old_name: str, new_name: str): 
        self.rename(old_name, "sample")
        self.rename("sample", new_name)
        
    def check_duplicate_tab_names(self, tab_name: str, is_edit: bool) -> None:
        if tab_name in self._tab_dict:
            # is an edit
            if is_edit and tab_name == self.get():
                print("la tab esiste, ma è quella selezionata, dunque un edit")
                return
            
            print("la tab esiste e non puo essere inserita")
            raise ValueError