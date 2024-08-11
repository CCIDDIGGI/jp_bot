from model.home.HomeModel import HomeModel
from shared.footer.model.FooterModel import FooterModel
from shared.header.model.HeaderModel import HeaderModel
from shared.sidebar.model.SidebarModel import SidebarModel

from view.home.HomeView import HomeView
from shared.sidebar.view.SidebarView import SidebarView
from shared.header.view.HeaderView import HeaderView
from shared.footer.view.FooterView import FooterView

from controller.home.HomeController import HomeController
from shared.sidebar.controller.SidebarController import SidebarController
from shared.header.controller.HeaderController import HeaderController
from shared.footer.controller.FooterController import FooterController

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
        
        footer_view = FooterView(parent)
        footer_model = FooterModel()
        FooterController(footer_model, footer_view)