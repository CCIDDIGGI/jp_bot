from shared.header.model import HeaderModel
from model.home.HomeModel import HomeModel
from shared.sidebar.model.SidebarModel import SidebarModel
from view.home.HomeView import HomeView
from shared.sidebar.view.SidebarView import SidebarView
from shared.header.view import HeaderView
from controller.home.HomeController import HomeController
from shared.header.controller import HeaderController
from shared.sidebar.controller.SidebarController import SidebarController

class LoginModel():

    def navigate_to_home(self, parent) -> None:
        sidebar_model = SidebarModel()
        sidebar_view = SidebarView(parent)
        SidebarController(sidebar_model, sidebar_view)
        
        home_view = HomeView(parent)
        home_model = HomeModel()
        HomeController(home_model, home_view)

        header_view = HeaderView(parent)
        header_model = HeaderModel()
        HeaderController(header_model, header_view)
