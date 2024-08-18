from components.home.model.HomeModel import HomeModel
from components.shared.footer.model.FooterModel import FooterModel
from components.shared.header.model.HeaderModel import HeaderModel
from components.shared.sidebar.model.SidebarModel import SidebarModel

from components.tabs.main.controller.MainTabController import MainTabController
from components.tabs.main.model.MainTabModel import MainTabModel
from components.tabs.main.view.MainTabView import MainTabView
from components.home.view.HomeView import HomeView
from components.shared.sidebar.view.SidebarView import SidebarView
from components.shared.header.view.HeaderView import HeaderView
from components.shared.footer.view.FooterView import FooterView

from components.home.controller.HomeController import HomeController
from components.shared.sidebar.controller.SidebarController import SidebarController
from components.shared.header.controller.HeaderController import HeaderController
from components.shared.footer.controller.FooterController import FooterController

from services.MainTabService import MainTabService

class LoginModel():

    def navigate_to_home(self, parent) -> None:
        main_tab_view = MainTabView(parent)
        main_tab_model = MainTabModel()
        MainTabController(main_tab_model, main_tab_view)
        
        sidebar_model = SidebarModel()
        sidebar_view = SidebarView(parent)
        SidebarController(sidebar_model, sidebar_view)
        
        # home_view = HomeView(parent)
        # home_model = HomeModel()
        # HomeController(home_model, home_view)

        header_view = HeaderView(parent)
        header_model = HeaderModel()
        HeaderController(header_model, header_view)
        
        footer_view = FooterView(parent)
        footer_model = FooterModel()
        FooterController(footer_model, footer_view)