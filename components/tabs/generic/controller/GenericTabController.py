
from components.tabs.dto.tab_dto import TabDTO

class GenericTabController():
    instances = []
    
    def __init__(self, model, view, tab_dto: TabDTO) -> None:
        GenericTabController.instances.append(self)
        self.model = model
        self.view = view
        self.tab_dto = tab_dto
        self.model.set_controller(self)
        self.view.set_controller(self)
        
    def delete_tab(self) -> None:
        self.model.delete_tab(self.tab_dto)    
        
    def edit_tab(self) -> None:
        self.model.edit_tab(self.tab_dto)
        
    def redraw_tab(self):
        self.view.redraw_tab(self.tab_dto)