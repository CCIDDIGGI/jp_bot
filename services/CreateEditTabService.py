
from typing import Self
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

    
    def create_modal_components(self, parent) -> None:
        self.create_edit_tab_model = CreateEditTabModel(self)
        self.create_edit_tab_view = CreateEditTabView(parent)
        self.create_edit_tab_controller = CreateEditTabController(self.create_edit_tab_model, self.create_edit_tab_view)

    def destroy_modal_components(self) -> None:
        self.create_edit_tab_model = None
        self.create_edit_tab_view = None
        self.create_edit_tab_controller = None      