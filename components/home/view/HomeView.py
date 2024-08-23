import tkinter
from customtkinter import *
from components.custom.CTkScrollableDropdown import CTkScrollableDropdown 

class HomeView(CTkFrame):
    diff_value = 0
    maximum_threshold_value = 0
    # child of MainView -> parent argument is MainView
    def __init__(self, parent):
        self.parent = parent
        
        # main setup
        super().__init__(parent)
        self.grid(row=1, column=1, columnspan=2, sticky="nsew")
        self.radio_diff_var = tkinter.IntVar(value=1)
        self.entry_diff_var = tkinter.StringVar(value='10')
        self.entry_maximum_threshold_var = tkinter.StringVar(value='50')

        # widgets
        lbl_diff = CTkLabel(self, width=300, text="Minimum price difference between the first and second cheapest listings")
        radio_diff_perc = CTkRadioButton(self, text="Percentage", variable=self.radio_diff_var, value=1,
                                          command=self.set_diff_type)
        radio_diff_flat = CTkRadioButton(self, text="Flat value", variable=self.radio_diff_var, value=2,
                                         command=self.set_diff_type)
        self.entry_diff = CTkEntry(self, width=150, textvariable=self.entry_diff_var)
        lbl_maximum_threshold = CTkLabel(self, width=300, text="Maximum threshold amount (EUR) that the software can add to the cart")
        self.entry_maximum_threshold = CTkEntry(self, width=150, textvariable=self.entry_maximum_threshold_var)
        self.lbl_diff_err = CTkLabel(self, width=300, text="Please insert only numerical values!")
        self.lbl_maximum_threshold_err = CTkLabel(self, width=300, text="Please insert only numerical values!")
        self.entry_exp = CTkEntry(self, width=300)
        btn_exp = CTkButton(self, text = "Get all listings for current expansion", state="disabled", command=self.set_listings_exp_id)
        self.btn_start_fetch = CTkButton(self, text = "Start process", state="disabled", command=self.start_fetch)
        self.btn_stop_fetch = CTkButton(self, text = "Stop process", state="disabled", command=self.stop_fetch)
        # moved down temporarly
        self.scr_drpd = CTkScrollableDropdown(self.entry_exp,
                                              command=lambda e: 
                                                  self.entry_exp.delete(0,'end') 
                                                  or self.entry_exp.insert(0, e) 
                                                  or btn_exp.configure(state="normal")
                                                  or self.btn_start_fetch.configure(state="normal"),
                                              autocomplete=True) 
        self.lbl_fetch_status = CTkLabel(self, width=300, text="")
        
        # widgets callback
        self.entry_diff_var.trace_add("write", self.try_parse_diff_var)
        self.entry_maximum_threshold_var.trace_add("write", self.try_parse_maximum_threshold_var)
        
        # widgets rendering
        lbl_diff.place(x=100, y=50)
        radio_diff_perc.place(x=100, y=100)
        radio_diff_flat.place(x=250, y=100)
        self.entry_diff.place(x=100, y=150)
        lbl_maximum_threshold.place(x=100, y=200)
        self.entry_maximum_threshold.place(x=100, y=250)
        self.entry_exp.place(x=100, y=300)
        btn_exp.place(x=400, y=300)
        self.btn_start_fetch.place(x=100, y=350)
        self.btn_stop_fetch.place(x=300, y=350)
        self.lbl_fetch_status.place(x=100, y=400)
        
    def set_controller(self, controller) -> None:
        self.controller = controller
        
    def initialize_variables(self) -> None:
        self.exp_list = self.controller.get_expansions_list()
        self.scr_drpd.configure(values=self.exp_list)  
        # hard coded for now, in the future it will fetch those values from a config file or page 
        self.controller.assign_default_values(10, 50)

    def set_diff_type(self) -> None:
        self.controller.set_diff_type(self.radio_diff_var.get())

    def try_parse_diff_var(self, *args) -> None:
        try:
            # replace 0 with settings default value
            self.diff_value = int(self.entry_diff_var.get()) if self.entry_diff_var.get() else 0
            # probably going to be moved from here
            self.controller.set_diff_value(self.diff_value)
            self.lbl_diff_err.place_forget()
        except ValueError:
            self.lbl_diff_err.place(x=250, y=150)
            
    def try_parse_maximum_threshold_var(self, *args) -> None:
        try:
            # replace 0 with settings default value
            self.maximum_threshold_value = int(self.entry_maximum_threshold_var.get()) if self.entry_maximum_threshold_var.get() else 0
            # probably going to be moved from here
            self.controller.set_maximum_threshold_value(self.maximum_threshold_value)
            self.lbl_maximum_threshold_err.place_forget()
        except ValueError:
            self.lbl_maximum_threshold_err.place(x=250, y=250)      

    def set_listings_exp_id(self) -> None:
        if self.entry_exp.get():    
            self.controller.set_exp_id_by_exp_name(self.entry_exp.get())
        
    def start_fetch(self) -> None:
        if self.controller:
            self.controller.start_fetch()
            self.btn_start_fetch.configure(state="disabled")
            self.btn_stop_fetch.configure(state="normal")

    def stop_fetch(self) -> None:
        if self.controller:
            self.controller.stop_fetch()
            self.btn_start_fetch.configure(state="normal")
            self.btn_stop_fetch.configure(state="disabled")
    
    def change_btn_configuration(self) -> None:
        self.btn_start_fetch.configure(state="normal")
        self.btn_stop_fetch.configure(state="disabled")
    
    def config_status_text(self, msg: str) -> None:
        self.lbl_fetch_status.configure(text=msg)        
