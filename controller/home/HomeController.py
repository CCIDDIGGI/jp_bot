
class HomeController():

    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view
        self.view.set_controller(self)

    def printaz(self) -> None:
        self.model.printaze()