from components.shared.modals.create_edit_tab.model.CreateEditTabModel import CreateEditTabModel
from components.shared.modals.create_edit_tab.view.CreateEditTabView import CreateEditTabView
from components.shared.modals.create_edit_tab.controller.CreateEditTabController import CreateEditTabController

class SidebarModel():
    
    def __init__(self) -> None:
        pass
            
    def open_new_tab_modal(self, parent) -> None:
        self.create_edit_tab_model = CreateEditTabModel()
        self.create_edit_tab_view = CreateEditTabView(parent)
        self.create_edit_tab_controller = CreateEditTabController(self.create_edit_tab_model, self.create_edit_tab_view)
        
    def close_new_tab_modal(self) -> None:
        self.create_edit_tab_model = None
        self.create_edit_tab_view = None
        self.create_edit_tab_controller = None  