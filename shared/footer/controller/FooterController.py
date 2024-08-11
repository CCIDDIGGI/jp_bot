
class FooterController():

    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view
        self.view.set_controller(self)
        self.model.set_controller(self)
