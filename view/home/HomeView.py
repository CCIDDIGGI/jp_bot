from customtkinter import *
from custom.CTkScrollableDropdown import CTkScrollableDropdown 

class HomeView(CTkFrame):
    
    # child of MainView -> parent argument is MainView
    def __init__(self, parent):
        # main setup
        super().__init__(parent)
        self.place(relx = 0.251, rely = 0, relwidth = 0.75, relheight = 1)

        # widgets
        btn = CTkButton(self, text = "TEST API!", command = self.test_api)
        entry_exp = CTkEntry(self, width=300)
        self.scr_drpd = CTkScrollableDropdown(entry_exp,
                                              command=lambda e: entry_exp.insert(0, e),
                                              autocomplete=True)
        
        # widgets rendering
        btn.place(x = 300, y = 20)
        entry_exp.place(x=400, y=400)

    def set_controller(self, controller) -> None:
        self.controller = controller
        
    # check if this is correct in mvc
    def initialize_variables(self) -> None:
        self.exp_list = self.controller.get_expansions_list()
        self.scr_drpd.configure(values=self.exp_list)

    def test_api(self) -> None:
        self.controller.test_api()
        


    # def test_api(self):

    #     headers = {
    #         'Authorization': f'Bearer {BearerToken.TOKEN.value}'
    #     }

    #     payload = {
    #         "product_id": 233952244,
    #         "quantity": 1,
    #         "via_cardtrader_zero": True,
    #         "billing_address": {
    #             "name": "name surname",
    #             "street": "via del bulo 00",
    #             "zip": "50143",
    #             "city": "firenze",
    #             "state_or_province": "FI",
    #             "country_code": "IT",
    #             "phone": "123456789"
    #         },
    #         "shipping_address": {
    #             "name": "name surname",
    #             "street": "via del bulo 00",
    #             "zip": "50143",
    #             "city": "firenze",
    #             "state_or_province": "FI",
    #             "country_code": "IT"
    #         }
    #     }

    #     response = requests.post(CartApi.ADD_PRODUCT_TO_CART.value, json=payload, headers=headers)

    #     if response.status_code == 200:
    #         print("SUCCESS")
    #     else:
    #         print(response.status_code, response.text)
