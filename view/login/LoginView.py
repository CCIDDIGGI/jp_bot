import tkinter
from customtkinter import *
from enums.api.ApiEnum import *

class LoginView(CTkFrame):  

    # child of MainView -> parent argument is MainView
    def __init__(self, parent):
        self.parent = parent

        # main setup
        super().__init__(parent)
        self.place(relwidth = 1, relheight = 1)
        self.auth_var = tkinter.StringVar()

        # widgets
        lbl = CTkLabel(self, 1, 1, 2, bg_color = "red", text = "Please enter your CardTrader personal Auth Token")
        self.auth_entry = CTkEntry(self, placeholder_text = "Auth Token...", textvariable=self.auth_var)
        self.btn = CTkButton(self, 20, 30, command = self.navigate_to_home, text = "Login", state = "disabled")
        
        # widgets callback
        self.auth_var.trace_add("write", self.check_auth_btn_state)

        # widgets rendering
        lbl.pack()
        self.auth_entry.pack()
        self.btn.pack()

    # setting controller (LoginController)
    def set_controller(self, controller) -> None:
        self.controller = controller
        
    def check_auth_btn_state(self, *args) -> None:      
        self.btn.configure(state = "normal" if self.auth_var.get() else "disabled")
        
    def navigate_to_home(self):
        self.controller.navigate_to_home(self.parent)
        self.pack_forget()
