import tkinter
from customtkinter import *

class MainTabView(CTkTabview):
    
    # child of MainView -> parent argument is MainView
    def __init__(self, parent):
        
        # main setup
        super().__init__(parent)
        self.parent = parent
        
        self.grid(row=1, column=1, sticky='nsew')