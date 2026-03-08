class Skill:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class SupportCard:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

class RaceResult:
    def __init__(self, race_name, position):
        self.race_name = race_name
        self.position = position

class SuccessionCharaInfo:
    def __init__(self, character_name, details):
        self.character_name = character_name
        self.details = details

class Uma:
    def __init__(self, name, skills, support_cards):
        self.name = name
        self.skills = skills  # list of Skill
        self.support_cards = support_cards  # list of SupportCard

class UmaCollection:
    def __init__(self):
        self.umas = []  # list of Uma

    def add_uma(self, uma):
        self.umas.append(uma)

    def remove_uma(self, uma):
        self.umas.remove(uma)

    def get_all_umas(self):
        return self.umas

    def find_uma_by_name(self, name):
        for uma in self.umas:
            if uma.name == name:
                return uma
        return None

    def display_collection(self):
        for uma in self.umas:
            print(f'Uma Name: {uma.name} - Skills: {[skill.name for skill in uma.skills]}')