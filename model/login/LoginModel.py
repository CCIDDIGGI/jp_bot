
from controller.home.HomeController import HomeController
from model.home.HomeModel import HomeModel
from view.home.HomeView import HomeView


class LoginModel():

    def navigate_to_home(self, parent) -> None:
        home_view = HomeView(parent)
        home_model = HomeModel()
        HomeController(home_model, home_view)
