import json
import os

class StorageManager:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(base_dir, "..", "data", "Student_data.json")

    def load(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                return json.load(file)
        return {}

    def save(self, data):
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)   