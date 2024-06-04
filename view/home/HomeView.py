from customtkinter import *

class HomeView(CTkFrame):

    # child of MainView -> parent argument is MainView
    def __init__(self, parent):

        # main setup
        super().__init__(parent)
        self.place(relx = 0.2, y = 100)

        # widgets
        btn = CTkButton(self, text = "open window!", command = self.open_window)
        btn.place(x = 20, y = 20)


    def open_window(self):
        print("CLICKED!")
    