
class LoginController():

    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view
        self.view.set_controller(self)

    def navigate_to_home(self, parent) -> None:
        self.model.navigate_to_home(parent)