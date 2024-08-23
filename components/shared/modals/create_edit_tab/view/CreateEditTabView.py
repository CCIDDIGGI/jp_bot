from customtkinter import *
from components.custom.CTkScrollableDropdown import CTkScrollableDropdown 

class CreateEditTabView(CTkFrame):
    
    def __init__(self, parent):
        self.parent = parent
        
        # main setup
        super().__init__(parent)
        self.configure(fg_color = "red")
        self.parent.disable_frames()
        self.grid(row=1, column=1, sticky='nsew')
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((0,1,2,3), weight=1)
        
        self.values = ["Pokémon", "Magic: The Gathering"]
        
        # widgets
        self.lbl_tcg = CTkLabel(self, text="Choose a TCG") 
        self.om_tcg = CTkOptionMenu(self)
        self.drpd_tcg = CTkScrollableDropdown(self.om_tcg,
                                        values=self.values)   
        self.btn_cancel = CTkButton(self, text="Cancel", command=self.cancel_procedure)
        self.btn_add = CTkButton(self, text="Add", command=self.add_tab)
        
        # widgets callback     
        
        # widgets rendering       
        self.lbl_tcg.grid(row=1, column=0) 
        self.om_tcg.grid(row=1, column=1)
        self.btn_cancel.grid(row=3, column=0)
        self.btn_add.grid(row=3, column=1)
        
    def cancel_procedure(self) -> None:
        self.parent.enable_frames()
        self.destroy()
    
    def add_tab(self) -> None:
        pass