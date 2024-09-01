
from services.CreateEditTabService import CreateEditTabService

class SidebarModel():
    
    def __init__(self) -> None:
        self.create_edit_tab_service = CreateEditTabService()
            
    def open_new_tab_modal(self, parent) -> None:
        self.create_edit_tab_service.create_modal_components(parent, True)