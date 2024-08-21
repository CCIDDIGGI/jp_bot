from typing import Self

class MainTabModel():

    _instance = None
    
    def __new__(cls, *args, **kwargs) -> Self:
        if cls._instance is None:
            cls._instance = super(MainTabModel, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self) -> None:
        pass
    
    def set_controller(self, controller) -> None:
        self.controller = controller
    
    def add_new_tab(self) -> None:
        pass
        
    