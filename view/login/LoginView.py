import requests
import pywhatkit

from customtkinter import *

from enums.api.ApiEnum import *

class LoginView:    
    
    def __init__(self) -> None:
        pass 


    def greet_event(self):
        print("CLICKED")
        print(self.get_info("https://api.cardtrader.com/api/v2/info", "eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJjYXJkdHJhZGVyLXByb2R1Y3Rpb24iLCJzdWIiOiJhcHA6OTc5MyIsImF1ZCI6ImFwcDo5NzkzIiwiZXhwIjo0ODcxOTA1MjYxLCJqdGkiOiIwMTdjNDZiOC05NmQ1LTQ0NzMtYTA3OC02YzEyY2Q1MDA2MjMiLCJpYXQiOjE3MTYyMzE2NjEsIm5hbWUiOiJUaW5hcmkgQXBwIDIwMjQwNDAzMjIxNTUwIn0.u_QsTlQErxV6LWrD0y2r5AMNoTds5qxTT2QaHVNwO_BxxS3mwEMwAg-muMOGJc6VuXb9UOBqTtdZdgmxHO65GV9NNn0xFbTgtZUTkHMrpNPXFeYXA8SxSv3jXOfg4agrC_aO5DekGJ2qoHJuXwaqdzbNln39wJmfsOnMVwVrmq5nbNjgn5LI6CEFk2Ri4sAe01dyYTGk0xPlbr_m63rrl5ridcFSlE3H2LXfkocbnXoLDEqgd9Z6HjAtqGTnd15PrQeTgBevvarrdnrQAtbt-eaXHMtQM2HJ6OgG8Q-6Jc3yU2P3A29Hs2YsqO-d8ZsEqIIPGQg1MurvtKt7CtMjeQ"))

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

        btn = CTkButton(app, text="Prova!", command=self.greet_event)
        btn.place(relx=0.2, rely=0.2, anchor="center")
        
        btn2 = CTkButton(app, text="add to cart!", command= self.add_product_to_cart)
        btn2.place(relx=0.5, rely=0.5, anchor="center")

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