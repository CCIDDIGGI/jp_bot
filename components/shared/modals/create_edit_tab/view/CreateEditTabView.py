import tkinter
from customtkinter import *
from components.custom.CTkScrollableDropdown import CTkScrollableDropdown 

class CreateEditTabView(CTkFrame):
    
    def __init__(self, parent):
        self.parent = parent
        
        # main setup
        super().__init__(parent)
        self.configure(fg_color = "red")
        # self.parent.disable_frames()
        self.grid(row=1, column=1, sticky='nsew')
        self.grid_columnconfigure((0,1,2,3), weight=1, uniform='column')
        self.grid_rowconfigure(0, weight=1, uniform='row')
        self.grid_rowconfigure((1,2,3,4), weight=1, uniform='row')
        
        self.values = ["Pokémon", "Magic: the Gathering"]
        self.title = "TITLE TODO"
        self.radio_diff_var = tkinter.IntVar(value=1)
        self.entry_diff_var = tkinter.StringVar(value='10')
        self.entry_maximum_threshold_var = tkinter.StringVar(value='50')
        
        # widgets
        self.lbl_title = CTkLabel(self, text=self.title) 
        self.lbl_name = CTkLabel(self, text="Enter a tab name") 
        self.entry_name = CTkEntry(self)

        self.lbl_tcg = CTkLabel(self, text="Choose a TCG") 
        self.om_tcg = CTkOptionMenu(self)
        self.drpd_tcg = CTkScrollableDropdown(self.om_tcg,
                                        values=self.values,
                                        command=self.get_expansions_by_tcg)  
        
        self.lbl_exp = CTkLabel(self, text="Choose an expansion from the list") 
        self.entry_exp = CTkEntry(self)
        self.drpd_exp = CTkScrollableDropdown(self.entry_exp,
                                              command=lambda e: 
                                                  self.entry_exp.delete(0,'end') 
                                                  or self.entry_exp.insert(0, e),
                                              autocomplete=True) 
        self.btn_cancel = CTkButton(self, text="Cancel", command=self.cancel_procedure)
        self.btn_add = CTkButton(self, text="Add", command=self.add_tab)

        self.lbl_diff = CTkLabel(self, text="Minimum price difference between the first and second cheapest listings", wraplength=200) 
        self.radio_diff_perc = CTkRadioButton(self, text="Percentage", variable=self.radio_diff_var, value=1,
                                          )
        self.radio_diff_flat = CTkRadioButton(self, text="Flat value", variable=self.radio_diff_var, value=2,
                                         )
        self.entry_diff = CTkEntry(self)
        
        # widgets callback     

        # widgets rendering  
        self.lbl_title.grid(row=0, column=0)
        self.lbl_name.grid(row=1, column=0)     
        self.entry_name.grid(row=1, column=1)  
        self.lbl_tcg.grid(row=2, column=0) 
        self.om_tcg.grid(row=2, column=1)
        self.lbl_exp.grid(row=3, column=0)
        self.entry_exp.grid(row=3, column=1)
        self.lbl_diff.grid(row=1, column=2, sticky='nsew')     
        self.entry_diff.grid(row=1, column=3)  

        self.btn_cancel.grid(row=4, column=1)
        self.btn_add.grid(row=4, column=2)

    def set_controller(self, controller) -> None:
        self.controller = controller

    def init_get_exp(self) -> None:
        self.get_expansions_by_tcg(self.values[0])

    def get_expansions_by_tcg(self, choice: str) -> None:
        self.controller.get_expansions_by_tcg(choice)
        self.om_tcg.set(choice)

    def set_expansions_by_tcg(self, exp: list) -> None:
        self.drpd_exp.configure(values=exp)
        
    def cancel_procedure(self) -> None:
        # self.parent.enable_frames()
        self.controller.cancel_procedure()
        self.destroy()
    
    def add_tab(self) -> None:
        pass