import tkinter
from typing import Self
from customtkinter import *

class MainTabView(CTkTabview):
    _instance = None
    
    def __new__(cls, *args, **kwargs) -> Self:
        if cls._instance is None:
            cls._instance = super(MainTabView, cls).__new__(cls)
        return cls._instance
    
    # child of MainView -> parent argument is MainView
    def __init__(self, parent):
        
        # main setup
        if not hasattr(self, '_initialized') or not self._initialized:
            super().__init__(parent)
            self.parent = parent
            
            self.grid(row=1, column=1, sticky='nsew')
            
            # initialized
            self._initialized = True