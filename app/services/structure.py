import json


class LargeJsonHandler:
    def __init__(self):
        self.data = None
        self.load_data()

    def load_data(self):
        with open('inverted_index.json', 'r') as file:
            self.data = json.load(file)

    @staticmethod
    def write_json(inverted_index: dict):
        with open('inverted_index.json', 'w') as file:
            json.dump(inverted_index, file)

    def get_value(self, key):
        return self.data.get(key)
