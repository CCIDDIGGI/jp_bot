import tkinter
import requests
from customtkinter import *
from enums.api.ApiEnum import *
from view.home.HomeView import HomeView
from view.shared.sidebar.SidebarView import SidebarView

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
        
    def check_auth_btn_state(self, *args):      
        self.btn.configure(state = "normal" if self.auth_var.get() else "disabled")
        
    def navigate_to_home(self):
        SidebarView(self.parent)
        HomeView(self.parent)
        self.destroy()

    def add_product_to_cart(self):
        try:
            self.post_product_to_cart()
        except Exception as exc:
            print(exc)

    def navigate(self):
        return

    
    def get_info(self, url, token):

        headers = {
            'Authorization': f'Bearer {token}'
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:   
            return response.status_code, response.text  