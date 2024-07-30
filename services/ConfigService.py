import os

class ConfigService():
    cfg_file_dir = 'C:\\jp_bot_config'
    cfg_file_name = 'jp_bot_config.txt'
    cfg_file_path = os.path.join(cfg_file_dir, cfg_file_name)
    auth_token = ''
    remember_var = 'off'

    def __init__(self) -> None:
        self.init_cfg()

    def init_cfg(self) -> None:
        self.check_for_cfg_file_dir()
        self.check_for_cfg_file()
        with open(self.cfg_file_path, 'a') as file:
            file.write(f"Remember auth token: {self.remember_var}")  

    def set_auth_token(self, token: str) -> None:
        self.auth_token = token
        print(f"auth token is {self.auth_token}")

    def get_auth_token(self) -> str:
        return self.auth_token
    
    def write_login_config(self, remember: str) -> None:
        self.check_for_cfg_file_dir()
        self.check_for_cfg_file()
        print(f"remember me is set to> {remember}")

    def check_for_cfg_file_dir(self) -> None:
        if not os.path.exists(self.cfg_file_dir):
            os.makedirs(self.cfg_file_dir)
            with open(self.cfg_file_path, 'w') as file:
                file.write("-----Jeff Pesos Bot Configuration File-----\n\n")           

    def check_for_cfg_file(self) -> None:
        if not os.path.exists(self.cfg_file_path):     
            with open(self.cfg_file_path, 'w') as file:
                file.write("-----Jeff Pesos Bot Configuration File-----\n\n")