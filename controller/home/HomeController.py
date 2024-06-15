
class HomeController():

    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view
        self.view.set_controller(self)
        self.view.initialize_variables()

    def test_api(self) -> None:
        self.model.test_api()
        
    def get_expansions(self) -> list:
        return self.model.get_expansions()