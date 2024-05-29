import requests
import pywhatkit

from customtkinter import *

from enums.api.ApiEnum import *
from view.home.HomeView import HomeView

class LoginView:  

    def __init__(self):
        global login_view
        login_view = CTk()
        login_view.geometry("500x400") 

        btn3 = CTkButton(login_view, text="navigate", command= self.navigate)
        btn3.place(x = 300, y = 30)
        
        btn2 = CTkButton(login_view, text="add to cart!", command= self.add_product_to_cart)
        btn2.place(relx=0.5, rely=0.5, anchor="center")
        
        cmb = CTkComboBox(login_view, values=['A', 'B', 'C', 'D'])
        cmb.place(x = 20, y = 20)

        login_view.mainloop()  
        
        
         

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
        prova = HomeView()
        login_view.destroy()

    
    def get_info(self, url, token):

        headers = {
            'Authorization': f'Bearer {token}'
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:   
            return response.status_code, response.text  