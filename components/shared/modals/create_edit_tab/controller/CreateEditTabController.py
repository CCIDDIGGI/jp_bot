
class CreateEditTabController():
    
    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view
        self.view.set_controller(self)
        self.model.set_controller(self)
        self.view.init_get_exp()

    def cancel_procedure(self) -> None:
        self.model.cancel_procedure()

    def get_expansions_by_tcg(self, choice: str) -> None:
        self.model.get_expansions_by_tcg(choice)

    def set_expansions_by_tcg(self, exp: list) -> None:
        self.view.set_expansions_by_tcg(exp)
        
    def add_new_tab(self, tab_dto) -> None:
        self.model.add_new_tab(tab_dto)
        