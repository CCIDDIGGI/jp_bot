import requests
import pywhatkit

from customtkinter import *

from enums.api.ApiEnum import *
from view.home.HomeView import HomeView

class LoginView:    
    
    def __init__(self) -> None:
        pass 

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

    def init_view(self):

        app = CTk()
        app.geometry("500x400") 

        btn1 = CTkButton(app, text="MOVE TO PAGE2", command= HomeView.init_view)
        btn1.place(x = 100, y = 300)
        
        btn2 = CTkButton(app, text="add to cart!", command= self.add_product_to_cart)
        btn2.place(relx=0.5, rely=0.5, anchor="center")
        
        cmb = CTkComboBox(app, values=['A', 'B', 'C', 'D'])
        cmb.place(x = 20, y = 20)

        app.mainloop()
    
    def get_info(self, url, token):

        headers = {
            'Authorization': f'Bearer {token}'
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:   
            return response.status_code, response.text  