from customtkinter import *

class AuthView:    
    
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        pass
    
    def get_instance():
        if not AuthView._instance:
            AuthView._instance = AuthView()
        return AuthView._instance
    
    def create_view(self): 
        auth_view = CTk()
        auth_view.geometry("500x400")
        auth_view.mainloop()