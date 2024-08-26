from customtkinter import *
from components.auth.controller.LoginController import LoginController
from components.auth.model.LoginModel import LoginModel
from components.auth.view.LoginView import LoginView

class MainView(CTk):
    # this should be populated with data from
    # a db (something like an "options" table)
    # for now, it is hard coded
    def __init__(self):
        # main setup
        super().__init__()
        self.title("Jeff Pesos Card Bot Alpha ver 1.0.1")
        self.get_geometry()
        self.grid_columnconfigure((0,2), weight=1, uniform='MainView')
        self.grid_columnconfigure(1, weight=3, uniform='MainView')
        self.grid_rowconfigure((0,2), weight=1, uniform='MainView')
        self.grid_rowconfigure(1, weight=10, uniform='MainView')

        # widgets
        login_view = LoginView(self)
        login_model = LoginModel()
        LoginController(login_model, login_view)
        
        # widgets callback

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
                
    def disable_frames(self) -> None:
        frames = [child for child in self.winfo_children() if isinstance(child, CTkFrame) 
                  or isinstance(child, CTkTabview)]
        for frame in frames:
            if frame.winfo_name() != "!createedittabview":
                frame.configure(fg_color="#333333")
                for widget in frame.winfo_children():
                    widget.configure(state="disabled")

    def enable_frames(self) -> None:
        frames = [child for child in self.winfo_children() if isinstance(child, CTkFrame) 
                  or isinstance(child, CTkTabview)]
        for frame in frames:
            if frame.winfo_name() != "!createedittabview":
                frame.configure(fg_color="#333333")
                for widget in frame.winfo_children():
                    widget.configure(state="normal")

