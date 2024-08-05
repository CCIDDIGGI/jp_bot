
from controller.home.HomeController import HomeController
from controller.shared.sidebar.SidebarController import SidebarController
from model.home.HomeModel import HomeModel
from model.shared.sidebar.SidebarModel import SidebarModel
from view.home.HomeView import HomeView
from view.shared.sidebar.SidebarView import SidebarView


class LoginModel():

    def navigate_to_home(self, parent) -> None:
        # removed sidebar for alpha version because shipping address is not required
        # sidebar_model = SidebarModel()
        # sidebar_view = SidebarView(parent)
        # SidebarController(sidebar_model, sidebar_view)
        
        home_view = HomeView(parent)
        home_model = HomeModel()
        HomeController(home_model, home_view)
