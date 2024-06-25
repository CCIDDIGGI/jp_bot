
class HomeController():

    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view
        self.view.set_controller(self)
        self.view.initialize_variables()
        
    def get_expansions_list(self) -> list:
        return self.model.get_mtg_exp_list()
    
    def set_diff_type(self, diff_type: int) -> None:
        self.model.set_diff_type(diff_type)

    def set_diff_value(self, diff_value: int) -> None:
        self.model.set_diff_value(diff_value)

    def get_exp_id_by_exp_name(self, exp_name: str) -> int:
        return self.model.get_exp_id_by_exp_name(exp_name)
    
    def get_listings_by_exp_id(self, exp_id: int) -> None:
        self.model.get_listings_by_exp_id(exp_id)