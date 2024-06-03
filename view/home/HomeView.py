from customtkinter import *

from view.login.LoginView import LoginView

class HomeView(CTk):

    def __init__(self, title, size):

        # main setup
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])

        # widgets
        btn = CTkButton(self, text = "open window!", command = self.open_window)
        btn.place(x = 20, y = 20)

        # run
        self.mainloop()

    def open_window(self):
        LoginView()
        print("CLICKED!")
    