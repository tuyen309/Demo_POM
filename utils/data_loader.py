import yaml

class DataLoader:
    @staticmethod
    def load_yaml(file_path):
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
