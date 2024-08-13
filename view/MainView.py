import time
from customtkinter import *
from controller.login.LoginController import LoginController
from model.login.LoginModel import LoginModel
from view.login.LoginView import LoginView
from shared.modals.loading_screen.LoadingScreenService import LoadingScreenService

class MainView(CTk):
    # this should be populated with data from
    # a db (something like an "options" table)
    # for now, it is hard coded
    def __init__(self):

        # main setup
        super().__init__()
        self.title("Jeff Pesos Card Bot Alpha ver 1.0.1")
        self.get_geometry()
        self.grid_columnconfigure(0, weight=1, uniform='a')
        self.grid_columnconfigure(1, weight=4, uniform='a')
        self.grid_rowconfigure((0,2), weight=1, uniform='a')
        self.grid_rowconfigure(1, weight=10, uniform='a')

        # widgets
        login_view = LoginView(self)
        login_model = LoginModel()
        LoginController(login_model, login_view)
        
        # run
        self.mainloop()

    def get_geometry(self) -> None:
        # min screen size is hard coded
        self.minsize(width=1024, height=576)
        geometry = f'{str(self.winfo_screenwidth())}x{str(self.winfo_screenheight())}'
        match geometry:
            case "1920x1080":
                self.geometry("1600x900")
            case "1536x864":
                self.geometry("1280x720")
            case _:
                self.geometry("1280x720")
