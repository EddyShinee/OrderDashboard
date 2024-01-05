import configparser
import json
import os


class ConfigurationManager:
    def __init__(self):
        self.config_data = {}
        pass

    def set_config_data(self, config_data):
        self.config_data = config_data

    def read_config(self):
        # Lấy đường dẫn của file Python hiện tại
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Tạo đường dẫn tương đối đến file config.ini
        config_path = os.path.join(current_dir, '..', 'config', 'config.ini')
        config = configparser.ConfigParser()
        try:
            config.read(config_path)
            print("Data config ==>")
            print(config.sections())
            print("----------------")
            for section in config.sections():
                self.config_data[section] = {}
                for option in config.options(section):
                    self.config_data[section][option] = config.get(section, option)
            self.set_config_data(self.config_data)
            
        except configparser.Error as e:
            print(f"Error reading config file: {e}")
            return None

        return self.config_data

    def is_sandbox(self):
        config_data = self.read_config()
        if 'ENV' in config_data and 'is_sandbox' in config_data['ENV']:
            return config_data['ENV']['is_sandbox'].lower() == 'true'
        return False  # Return False if 'is_sandbox' is not found or not 'True' in the configuration
