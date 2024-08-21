from customtkinter import *
from components.custom.CTkScrollableDropdown import CTkScrollableDropdown 

class CreateEditTabView(CTkFrame):
    
    def __init__(self, parent):
        
        # main setup
        super().__init__(parent)
        self.grid(row=1, column=1, sticky='nsew')
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((0,1,2,3), weight=1)
        
        # widgets
        self.lbl_tcg = CTkLabel(self, text="Choose a TCG") 
        self.entry_tcg = CTkEntry(self)
        self.drpd_tcg = CTkScrollableDropdown(self.entry_tcg,
                                        autocomplete=True)   
        
        # widgets callback     
        
        # widgets rendering       
        self.lbl_tcg.grid(row=1, column=0, sticky='nsew') 
        self.entry_tcg.grid(row=1, column=1, sticky='nsew')