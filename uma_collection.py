import json

class UmaCollection:
    def __init__(self, filepath='umas/data.json'):
        self.filepath = filepath
        self.uma_objects = []
        self.load_umas()

    def load_umas(self):
        try:
            with open(self.filepath, 'r') as file:
                self.uma_objects = json.load(file)
        except Exception as e:
            print(f'Error loading uma objects: {e}')

    def get_uma(self, uma_id):
        for uma in self.uma_objects:
            if uma.get('id') == uma_id:
                return uma
        return None

    def all_umas(self):
        return self.uma_objects

    # Additional methods to manage Uma objects can be added here.
