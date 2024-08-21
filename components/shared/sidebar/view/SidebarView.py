import tkinter
from customtkinter import *
from services.ConfigService import ConfigService

class SidebarView(CTkFrame):

    # child of MainView -> parent argument is MainView
    def __init__(self, parent):
        self.parent = parent
        self.config_service = ConfigService()

        # main setup
        super().__init__(parent)
        self.grid(row=1, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # self.entry_bill_name_var = tkinter.StringVar(value=self.config_service.config["Billing address name"])
        # self.entry_bill_street_var = tkinter.StringVar(value=self.config_service.config["Billing Street"])
        # self.entry_bill_zip_var = tkinter.StringVar(value=self.config_service.config["Billing zip"])
        # self.entry_bill_city_var = tkinter.StringVar(value=self.config_service.config["Billing city"])
        # self.entry_bill_state_or_province_var = tkinter.StringVar(value=self.config_service.config["Billing state or province"])
        # self.entry_bill_country_code_var = tkinter.StringVar(value=self.config_service.config["Billing country code"])
        # self.entry_bill_phone_var = tkinter.StringVar(value=self.config_service.config["Billing phone"])
        # self.entry_ship_name_var = tkinter.StringVar(value=self.config_service.config["Shipping name"])
        # self.entry_ship_street_var = tkinter.StringVar(value=self.config_service.config["Shipping street"])
        # self.entry_ship_zip_var = tkinter.StringVar(value=self.config_service.config["Shipping zip"])
        # self.entry_ship_city_var = tkinter.StringVar(value=self.config_service.config["Shipping city"])
        # self.entry_ship_state_or_province_var = tkinter.StringVar(value=self.config_service.config["Shipping state or province"])
        # self.entry_ship_country_code_var = tkinter.StringVar(value=self.config_service.config["Shipping country code"])

        # widgets
        # lbl_billing_info = CTkLabel(self, bg_color="red",text="Billing address informations")
        # lbl_bill_name = CTkLabel(self, text="Name:")
        # self.entry_bill_name = CTkEntry(self, width=150, textvariable=self.entry_bill_name_var)    
        # lbl_bill_street = CTkLabel(self, text="Street:")
        # self.entry_bill_street = CTkEntry(self, width=150, textvariable=self.entry_bill_street_var)    
        # lbl_bill_zip = CTkLabel(self, text="Zip code:")
        # self.entry_bill_zip = CTkEntry(self, width=150, textvariable=self.entry_bill_zip_var)    
        # lbl_bill_city = CTkLabel(self, text="City:")
        # self.entry_bill_city = CTkEntry(self, width=150, textvariable=self.entry_bill_city_var)    
        # lbl_bill_state_or_province = CTkLabel(self, text="State or province:")
        # self.entry_bill_state_or_province = CTkEntry(self, width=150, textvariable=self.entry_bill_state_or_province_var)    
        # lbl_bill_country_code = CTkLabel(self, text="Country code:")
        # self.entry_bill_country_code = CTkEntry(self, width=150, textvariable=self.entry_bill_country_code_var)    
        # lbl_bill_phone = CTkLabel(self, text="Phone:")
        # self.entry_bill_phone = CTkEntry(self, width=150, textvariable=self.entry_bill_phone_var)    

        # lbl_shipping_info = CTkLabel(self, bg_color="red",text="Shipping address informations")
        # lbl_ship_name = CTkLabel(self, text="Name:")
        # self.entry_ship_name = CTkEntry(self, width=150, textvariable=self.entry_ship_name_var)    
        # lbl_ship_street = CTkLabel(self, text="Street:")
        # self.entry_ship_street = CTkEntry(self, width=150, textvariable=self.entry_ship_street_var)    
        # lbl_ship_zip = CTkLabel(self, text="Zip code:")
        # self.entry_ship_zip = CTkEntry(self, width=150, textvariable=self.entry_ship_zip_var)    
        # lbl_ship_city = CTkLabel(self, text="City:")
        # self.entry_ship_city = CTkEntry(self, width=150, textvariable=self.entry_ship_city_var)    
        # lbl_ship_state_or_province = CTkLabel(self, text="State or province:")
        # self.entry_ship_state_or_province = CTkEntry(self, width=150, textvariable=self.entry_ship_state_or_province_var)    
        # lbl_ship_country_code = CTkLabel(self, text="Country code:")
        # self.entry_ship_country_code = CTkEntry(self, width=150, textvariable=self.entry_ship_country_code_var) 

        # self.btn_save = CTkButton(self, text="Save settings", command=self.save_settings)
        self.btn_add = CTkButton(self, text="Add Tab", command=self.open_new_tab_modal)

        # widgets rendering
        # lbl_billing_info.place(x=20, y=20)
        # lbl_bill_name.place(x=20, y=50)
        # self.entry_bill_name.place(x=80, y=50)
        # lbl_bill_street.place(x=20, y=80)
        # self.entry_bill_street.place(x=80, y=80)
        # lbl_bill_zip.place(x=20, y=110)
        # self.entry_bill_zip.place(x=80, y=110)
        # lbl_bill_city.place(x=20, y=140)
        # self.entry_bill_city.place(x=80, y=140)
        # lbl_bill_state_or_province.place(x=20, y=170)
        # self.entry_bill_state_or_province.place(x=130, y=170)
        # lbl_bill_country_code.place(x=20, y=200)
        # self.entry_bill_country_code.place(x=130, y=200)
        # lbl_bill_phone.place(x=20, y=230)
        # self.entry_bill_phone.place(x=80, y=230)
        # lbl_shipping_info.place(x=20, y=260)
        # lbl_ship_name.place(x=20, y=290)
        # self.entry_ship_name.place(x=80, y=290)
        # lbl_ship_street.place(x=20, y=320)
        # self.entry_ship_street.place(x=80, y=320)
        # lbl_ship_zip.place(x=20, y=350)
        # self.entry_ship_zip.place(x=80, y=350)
        # lbl_ship_city.place(x=20, y=380)
        # self.entry_ship_city.place(x=80, y=380)
        # lbl_ship_state_or_province.place(x=20, y=410)
        # self.entry_ship_state_or_province.place(x=130, y=410)
        # lbl_ship_country_code.place(x=20, y=440)
        # self.entry_ship_country_code.place(x=130, y=440)
        # self.btn_save.place(x=20, y=500)
        self.btn_add.grid(row=0, column=0)
      
    
    # setting controller (SidebarController)        
    def set_controller(self, controller) -> None:
        self.controller = controller

    def save_settings(self) -> None:
        settings = {        
            "Billing address name": self.entry_bill_name_var.get(),
            "Billing Street": self.entry_bill_street_var.get(),
            "Billing zip": self.entry_bill_zip_var.get(),
            "Billing city": self.entry_bill_city_var.get(),
            "Billing state or province": self.entry_bill_state_or_province_var.get(),
            "Billing country code": self.entry_bill_country_code_var.get(),
            "Billing phone": self.entry_bill_phone_var.get(),
            "Shipping name": self.entry_ship_name_var.get(),
            "Shipping street": self.entry_ship_street_var.get(),
            "Shipping zip": self.entry_ship_zip_var.get(),
            "Shipping city": self.entry_ship_city_var.get(),
            "Shipping state or province": self.entry_ship_state_or_province_var.get(),
            "Shipping country code": self.entry_ship_country_code_var.get()
        }
        self.config_service.write_address_config(settings)
        
    def open_new_tab_modal(self) -> None:
        self.controller.open_new_tab_modal(self.parent)