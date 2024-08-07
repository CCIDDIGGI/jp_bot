from customtkinter import *
from controller.login.LoginController import LoginController
from model.login.LoginModel import LoginModel
from view.login.LoginView import LoginView

class MainView(CTk):
    # this should be populated with data from
    # a db (something like an "options" table)
    # for now, it is hard coded
    def __init__(self):

        # main setup
        super().__init__()
        self.title("Jeff Pesos Card Bot Alpha ver 1.0.1")
        self.geometry("1280x720")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # widgets
        login_view = LoginView(self)
        login_model = LoginModel()
        LoginController(login_model, login_view)

        # run
        self.mainloop()

