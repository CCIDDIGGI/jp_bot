from components.shared.modals.create_edit_tab.model.CreateEditTabModel import CreateEditTabModel
from components.shared.modals.create_edit_tab.view.CreateEditTabView import CreateEditTabView
from components.shared.modals.create_edit_tab.controller.CreateEditTabController import CreateEditTabController

class SidebarModel():
    
    def __init__(self) -> None:
        pass
            
    def open_new_tab_modal(self, parent) -> None:
        create_tab_view = CreateEditTabView(parent)
        create_tab_model = CreateEditTabModel()
        CreateEditTabController(create_tab_model, create_tab_view)