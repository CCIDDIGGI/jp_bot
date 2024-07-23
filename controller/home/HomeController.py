
class HomeController():

    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view
        self.view.set_controller(self)
        self.model.set_controller(self)
        self.view.initialize_variables()
        
    def get_expansions_list(self) -> list:
        return self.model.get_mtg_exp_list()
    
    def set_diff_type(self, diff_type: int) -> None:
        self.model.set_diff_type(diff_type)

    def set_diff_value(self, diff_value: int) -> None:
        self.model.set_diff_value(diff_value)

    def set_maximum_threshold_value(self, maximum_threshold_value: int) -> None:
        self.model.set_maximum_threshold_value(maximum_threshold_value)

    def set_exp_id_by_exp_name(self, exp_name: str) -> None:
        self.model.set_exp_id_by_exp_name(exp_name)

    def start_fetch(self) -> None:
        self.model.start_fetch()

    def stop_fetch(self) -> None:
        self.model.stop_fetch()
    
    def change_btn_configuration(self) -> None:
        self.view.change_btn_configuration()
    
    def send_info_to_view(self, msg: str) -> None:
        self.view.config_status_text(msg)