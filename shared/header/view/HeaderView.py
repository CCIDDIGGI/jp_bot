from customtkinter import *

class HeaderView(CTkFrame):
    # child of MainView -> parent argument is MainView
    def __init__(self, parent):
        # main setup
        super().__init__(parent)
        self.grid(row=0, column=0, sticky="nsew")