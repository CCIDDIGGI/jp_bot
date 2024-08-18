

class SidebarController():
    
    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view
        self.view.set_controller(self)
        
    def add(self) -> None:
        self.model.add()