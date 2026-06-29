import yaml


class ConfigManager:

    def __init__(self,
                 config_path="configs/config.yaml"):

        with open(config_path, "r") as file:
            self.config = yaml.safe_load(file)

    def get(self):
        return self.config