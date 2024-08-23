from customtkinter import *
from services.HeaderService import HeaderService

class HeaderView(CTkFrame):
    # child of MainView -> parent argument is MainView
    def __init__(self, parent):
        self.header_service = HeaderService()
        
        # main setup
        super().__init__(parent)
        self.grid(row=0, column=0, columnspan=3, sticky="nsew")
        self.grid_rowconfigure(0, weight=1, uniform='header')
        self.grid_columnconfigure((0,4), weight=1, uniform='header')
        self.grid_columnconfigure((1,2,3), weight=1, uniform='header')
        self.lbl_name_var = self.header_service.get_username()
        
        # widgets
        self.lbl_logo = CTkLabel(self, text="Jeff pesos bot alpha ver 1.0.1", fg_color='blue')
        self.lbl_tab_1 = CTkLabel(self, text="tab 1", fg_color='yellow')
        self.lbl_tab_2 = CTkLabel(self, text="tab 2", fg_color='yellow')
        self.lbl_tab_3 = CTkLabel(self, text="tab 3", fg_color='yellow')
        self.lbl_name = CTkLabel(self, text=f"Welcome {self.lbl_name_var}", fg_color='red')
        
        # widgets callback
        
        # widgets rendering
        self.lbl_tab_1.grid(row=0, column=1, sticky='nsew')
        self.lbl_tab_2.grid(row=0, column=2, sticky='nsew')
        self.lbl_tab_3.grid(row=0, column=3, sticky='nsew')
        self.lbl_logo.grid(row=0, column=0, sticky='nsew')
        self.lbl_name.grid(row=0, column=4, sticky='nsew')

    # setting controller (HeaderController)
    def set_controller(self, controller) -> None:
        self.controller = controller