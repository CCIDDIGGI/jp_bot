from customtkinter import *

class GenericTabView(CTkFrame):
    
    def __init__(self, parent):
        
        super().__init__(parent)
        
        self.grid(row=1, column=1)
        
        # widgets
        self.lbl_prova = CTkLabel(self, text="prova")
        
        # widgets rendering
        self.lbl_prova.grid(row=1, column=1)