from customtkinter import *

class FooterView(CTkFrame):
    # child of MainView -> parent argument is MainView
    def __init__(self, parent):
        # main setup
        super().__init__(parent)
        self.grid(row=2, column=0, columnspan=3, sticky="nsew")
        
    # setting controller (FooterController)
    def set_controller(self, controller) -> None:
        self.controller = controller