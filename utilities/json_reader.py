import json
import os


class JsonReader:

    @staticmethod
    def read_json(file_path):

        # Ensure correct path handling across Windows/Linux
        base_path = os.path.dirname(os.path.dirname(__file__))
        full_path = os.path.join(base_path, file_path)

        with open(full_path, "r") as file:
            data = json.load(file)

        return data