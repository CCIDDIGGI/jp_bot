from customtkinter import *

from view.login.LoginView import LoginView

class MainView(CTk):

    # this should be populated with data from
    # a db (something like an "options" table)
    # for now, it is hard coded
    def __init__(self):

        # main setup
        super().__init__()
        self.title("Jeff Pesos Money Printer")
        self.geometry("1600x900")
        self.minsize(1280, 800)
        self.resizable(True, True)

        # widgets
        self.login_frame = LoginView(self)
        # self.home_frame = HomeView(self)

        # run
        self.mainloop()

