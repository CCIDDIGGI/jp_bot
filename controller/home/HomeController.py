
class HomeController():

    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view

    def print(self) -> None:
        self.model.print()