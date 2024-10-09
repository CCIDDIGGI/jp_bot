from customtkinter import *

class GenericTabView(CTkFrame):
    
    def __init__(self, parent):
        
        super().__init__(parent)
        self.configure(fg_color = "transparent")
        
        self.grid(row=1, column=1)
        
        # widgets
        self.lbl_prova = CTkLabel(self, text="prova")
        self.btn_delete_tab = CTkButton(self, text="Delete this tab", command=self.delete_tab)
        self.btn_edit_tab = CTkButton(self, text="Edit this tab", command=self.edit_tab)

        
        # widgets rendering
        self.lbl_prova.grid(row=1, column=1)
        self.btn_delete_tab.grid(row=2, column=1)
        self.btn_edit_tab.grid(row=3, column=1)
        
    def set_controller(self, controller) -> None:
        self.controller = controller
        
    def delete_tab(self) -> None:
        self.controller.delete_tab()
                
    def edit_tab(self) -> None:
        self.controller.edit_tab()