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
        self.title("Jeff Pesos Money Printer")
        self.geometry("1200x580")
        # self.minsize(1280, 800)
        self.resizable(True, True)

        # widgets
        login_view = LoginView(self)
        login_model = LoginModel()
        LoginController(login_model, login_view)

        # run
        self.mainloop()

