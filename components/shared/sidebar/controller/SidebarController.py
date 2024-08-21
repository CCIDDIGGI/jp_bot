

class SidebarController():
    
    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view
        self.view.set_controller(self)
        
    def open_new_tab_modal(self, parent) -> None:
        self.model.open_new_tab_modal(parent)