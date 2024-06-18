from customtkinter import *

from CTkScrollableDropdown import *

class HomeView(CTkFrame):
    
    # child of MainView -> parent argument is MainView
    def __init__(self, parent):
        # main setup
        super().__init__(parent)
        self.place(relx = 0.251, rely = 0, relwidth = 0.75, relheight = 1)

        # widgets
        self.cmb_exp = CTkComboBox(self, )
        btn = CTkButton(self, text = "TEST API!", command = self.test_api)

        self.scr_drpd = CTkScrollableDropdown(attach=self)
        
        # widgets rendering
        self.cmb_exp.place(x=150, y=250)
        btn.place(x = 300, y = 20)

    def set_controller(self, controller) -> None:
        self.controller = controller
        
    # check if this is correct in mvc
    def initialize_variables(self) -> None:
        self.exp_list = self.controller.get_expansions_list()
        self.cmb_exp.configure(values=self.exp_list)

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
