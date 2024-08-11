from customtkinter import *

from services.HeaderService import HeaderService

class HeaderView(CTkFrame):
    # child of MainView -> parent argument is MainView
    def __init__(self, parent):
        self.header_service = HeaderService()
        
        # main setup
        super().__init__(parent)
        self.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.grid_rowconfigure(0, weight=1, uniform='a')
        self.grid_columnconfigure((0,4), weight=1, uniform='a')
        self.grid_columnconfigure((1,2,3), weight=4, uniform='a')
        self.lbl_name_var = self.header_service.get_username()
        
        # widgets
        self.lbl_name = CTkLabel(self, text=f"Welcome {self.lbl_name_var}")
        
        # widgets callback
        
        # widgets rendering
        self.lbl_name.grid(row=0, column=4, sticky='nsew')

    # setting controller (HeaderController)
    def set_controller(self, controller) -> None:
        self.controller = controller