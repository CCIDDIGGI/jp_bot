import requests
import pywhatkit
from customtkinter import *
from enums.api.ApiEnum import *
from view.home.HomeView import HomeView

class LoginView(CTkFrame):  

    # child of MainView -> parent argument is MainView
    def __init__(self, parent):
        self.parent = parent

        # main setup
        super().__init__(parent)
        self.place(relwidth = 1, relheight = 1)

        # widgets
        lbl = CTkLabel(self, 1, 1, 2, bg_color = "red", text = "Please enter your CardTrader personal Auth Token")
        self.auth_entry = CTkEntry(self, placeholder_text = "Auth Token...")
        self.btn = CTkButton(self, 20, 30, command = self.navigate_to_home, text = "Login", state = "disabled")
        
        # widgets callback
        self.auth_entry.bind("<<KeyPress>>", self.check_auth_btn_state)

        # widgets rendering
        lbl.pack()
        self.auth_entry.pack()
        self.btn.pack()
        
    def check_auth_btn_state(self, event = None):
        print("Event triggered!")
        self.btn.configure(state = "normal" if self.auth_entry.get() else "disabled")
        self.auth_entry.configure(va)
        
    def navigate_to_home(self):
        HomeView(self.parent)
        self.destroy()

    def add_product_to_cart(self):
        try:
            self.post_product_to_cart()
        except Exception as exc:
            print(exc)

    def post_product_to_cart(self):
        
        headers = {
            'Authorization': f'Bearer {BearerToken.TOKEN.value}'
        }
        
        payload = {
            "product_id": 233952244,
            "quantity": 1,
            "via_cardtrader_zero": True,
            "billing_address": {
                "name": "name surname",
                "street": "via del bulo 00",
                "zip": "50143",
                "city": "firenze",
                "state_or_province": "FI",
                "country_code": "IT",
                "phone": "123456789"
            },
            "shipping_address": {
                "name": "name surname",
                "street": "via del bulo 00",
                "zip": "50143",
                "city": "firenze",
                "state_or_province": "FI",
                "country_code": "IT"
            }
        }

        response = requests.post(CartApi.ADD_PRODUCT_TO_CART.value, json=payload, headers=headers)
        
        if response.status_code == 200:
            pywhatkit.sendwhatmsg_instantly("+393453231789", "ADDED to cart", 15, True, 3)
        else:   
            print(response.status_code, response.text)

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