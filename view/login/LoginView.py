import tkinter
import webbrowser
from customtkinter import *
from enums.api.ApiEnum import *
from services.HeaderService import HeaderService
from services.ConfigService import ConfigService
from shared.modals.loading_screen.LoadingScreenService import LoadingScreenService

class LoginView(CTkFrame):  

    # child of MainView -> parent argument is MainView
    def __init__(self, parent):
        self.parent = parent
        self.config_service = ConfigService()
        self.header_service = HeaderService()
        self.loading_screen_service = LoadingScreenService(parent)
        # main setup
        super().__init__(parent)
        self.grid(row=0, column=0, rowspan=3, columnspan=2, sticky="nsew")
        self.auth_var = tkinter.StringVar(value=self.config_service.config["Auth token"])
        self.ckb_remember_var = tkinter.StringVar(value=self.config_service.config["Remember auth token"])
        
        # widgets
        lbl = CTkLabel(self, 1, 1, 2, bg_color = "red", text = "Please enter your CardTrader personal Auth Token")
        self.auth_entry = CTkEntry(self, placeholder_text = "Auth Token...", textvariable=self.auth_var)
        self.btn = CTkButton(self, 20, 30, command = self.init_navigate_to_home, text = "Login", state = "disabled")
        self.ckb_remember = CTkCheckBox(self, text="Remember my auth token", variable=self.ckb_remember_var,
                                         onvalue='on', offvalue='off')
        lbl_info = CTkLabel(self, text="Get your personal auth token from the link below, login first, if needed.")
        self.btn_to_auth_token = CTkButton(self, text="Navigate to https://www.cardtrader.com/docs/api/full/reference",
                                           command=lambda: webbrowser.open("https://www.cardtrader.com/docs/api/full/reference"))
        
        # widgets callback
        self.check_auth_btn_state()
        self.auth_var.trace_add("write", self.check_auth_btn_state)

        # widgets rendering
        lbl.place(x=400, y=50)
        self.auth_entry.place(x=400, y=100)
        self.btn.place(x=400, y=150)
        self.ckb_remember.place(x=550, y=150)
        lbl_info.place(x=400, y=200)
        self.btn_to_auth_token.place(x=400, y=250)

    # setting controller (LoginController)
    def set_controller(self, controller) -> None:
        self.controller = controller
        
    def check_auth_btn_state(self, *args) -> None:      
        self.btn.configure(state = "normal" if self.auth_var.get() else "disabled")
        
    def init_navigate_to_home(self) -> None:
        self.loading_screen_service.start_loading()
        # main thread
        self.navigate_to_home()
        self.loading_screen_service.stop_loading()
        
    def navigate_to_home(self):
        self.config_service.set_auth_token(self.auth_var.get())
        self.config_service.write_login_config(self.auth_var.get() ,self.ckb_remember_var.get())
        self.header_service.fetch_username()
        self.controller.navigate_to_home(self.parent)
        self.grid_forget()
    
