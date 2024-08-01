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
            self.write_to_file(self.default_config)
            return True  
        # if folder exists but not the config file
        if not os.path.exists(self.cfg_file_path):                       
            self.write_to_file(self.default_config) 
            return True
        return False
    
    def set_auth_token(self, token: str) -> None:
        self.auth_token = token

    def get_auth_token(self) -> str:
        return self.auth_token

    def init_cfg_dict(self) -> None:
        with open(self.cfg_file_path, 'r') as file:
            lines = file.readlines()
            for line in lines[2:]:
                key, value = line.split(":", 1)
                self.config[key] = value.strip()            
    
    def write_login_config(self, token: str, remember: str) -> None:
        # cancel current config content
        with open(self.cfg_file_path, 'w') as file:
            pass
        self.config["Remember auth token"] = remember
        if remember == 'on':
            self.config["Auth token"] = token
        else:
            self.config["Auth token"] = ""            
        self.write_to_file(self.config)   
    
    def write_address_config(self, settings: dict) -> None:
        # cancel current config content
        with open(self.cfg_file_path, 'w') as file:
            pass
        for key in settings:
            self.config[key] = settings[key]         
        self.write_to_file(self.config)  

    def write_to_file(self, dict: dict) -> None:
        with open(self.cfg_file_path, 'w') as file:
            file.write("-----Jeff Pesos Bot Configuration File-----\n\n")    
        for key in dict:
            with open(self.cfg_file_path, 'a') as file:
                file.write(f"{key}: {dict[key]}\n")         
            

