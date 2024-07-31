import os

class ConfigService():
    cfg_file_dir = 'C:\\jp_bot_config'
    cfg_file_name = 'jp_bot_config.txt'
    cfg_file_path = os.path.join(cfg_file_dir, cfg_file_name)
    default_config = {
        "Auth token": "",
        "Remember auth token": "off",
        "Billing address name": "",
        "Billing Street": "",
        "Billing zip": "",
        "Billing city": "",
        "Billing state or province": "",
        "Billing country code": "",
        "Billing phone": "",
        "Shipping name": "",
        "Shipping street": "",
        "Shipping zip": "",
        "Shipping city": "",
        "Shipping state or province": "",
        "Shipping country code": ""
    }

    config = {}

    def __init__(self) -> None:
        if not self.init_cfg_dir_and_file():
            self.init_cfg_dict()
        else: 
            self.config = self.default_config

    def init_cfg_dir_and_file(self) -> bool:
        # if folder does not exist
        if not os.path.exists(self.cfg_file_dir):
            os.makedirs(self.cfg_file_dir)
            # this snippet needs to be reusable, do a function
            # with open(self.cfg_file_path, 'w') as file:
            #     file.write("-----Jeff Pesos Bot Configuration File-----\n\n")    
            for key in self.default_config:
                with open(self.cfg_file_path, 'a') as file:
                    file.write(f"{key}: {self.default_config[key]}\n")    
            return True  
        # if folder exists but not the config file
        if not os.path.exists(self.cfg_file_path):                       
            # with open(self.cfg_file_path, 'w') as file:
            #     file.write("-----Jeff Pesos Bot Configuration File-----\n\n")    
            for key in self.default_config:
                with open(self.cfg_file_path, 'a') as file:
                    file.write(f"{key}: {self.default_config[key]}\n") 
            return True
        return False

    def init_cfg_dict(self) -> None:
        with open(self.cfg_file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                key, value = line.split(":", 1)
                self.config[key] = value.strip()            

    def set_auth_token(self, token: str) -> None:
        self.auth_token = token
        print(f"auth token is {self.auth_token}")

    def get_auth_token(self) -> str:
        return self.auth_token
    
    def write_login_config(self, remember: str) -> None:
        # cancel current config content
        with open(self.cfg_file_path, 'w') as file:
            pass
        self.config["Remember auth token"] = remember
        for key in self.config:
            with open(self.cfg_file_path, 'a') as file:
                file.write(f"{key}: {self.config[key]}\n")     
            

