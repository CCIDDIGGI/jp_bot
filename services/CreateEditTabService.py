
from typing import Self
from components.tabs.dto.tab_dto import TabDTO
from components.shared.modals.create_edit_tab.model.CreateEditTabModel import CreateEditTabModel
from components.shared.modals.create_edit_tab.view.CreateEditTabView import CreateEditTabView
from components.shared.modals.create_edit_tab.controller.CreateEditTabController import CreateEditTabController

class CreateEditTabService():

    _instance = None

    def __new__(cls, *args, **kwargs) -> Self:
        if cls._instance is None:
            cls._instance = super(CreateEditTabService, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self) -> None:
        self.create_edit_tab_model = None
        self.create_edit_tab_view = None
        self.create_edit_tab_controller = None

    
    def create_modal_components(self, parent, tab_data: TabDTO = None) -> None:
        self.create_edit_tab_model = CreateEditTabModel(self)
        if tab_data is None:
            self.create_edit_tab_view = CreateEditTabView(parent)
        else:
            self.create_edit_tab_view = CreateEditTabView(parent, tab_data)
        self.create_edit_tab_controller = CreateEditTabController(self.create_edit_tab_model, self.create_edit_tab_view)

    def destroy_modal_components(self) -> None:
        if self.create_edit_tab_view:
            self.create_edit_tab_view.grid_forget()  # Nascondi il frame dal layout
            self.create_edit_tab_view.destroy()      # Distruggi tutti i widget associati
            self.create_edit_tab_view = None         # Rimuovi il riferimento alla view

        self.create_edit_tab_model = None  # Rimuovi il riferimento al modello
        self.create_edit_tab_controller = None  # Rimuovi il riferimento al controller