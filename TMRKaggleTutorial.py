from dataclasses import dataclass

@dataclass(frozen=True)
class TMRKaggleTutorial:
    def __init__(self, dataset) -> None:
        self.dataset = [{'name': 'Linda',
            'characters_used': "['Link', 'Pikachu', 'Pikachu', 'Mario', 'Yoshi']",
            'wins': 5},
            {'name': 'Chris',
            'characters_used': "['Cloud', 'Meta Knight', 'Pikachu', 'Pikachu']",
            'wins': 1},
            {'name': 'Howard',
            'characters_used': "['Link', 'Megaman', 'Kirby']",
            'wins': 5},
            {'name': None,
            'characters_used': "['Bayonetta', 'Mario', 'Meta Knight']",
            'wins': 3},
            {'name': 'Chandler',
            'characters_used': "['Bayonetta', 'Pikachu', 'Kirby', 'Link', 'Kirby']",
            'wins': 3},
            {'name': 'Alex',
            'characters_used': "['Pikachu', 'Kirby', 'Cloud', 'Kirby']",
            'wins': 1},
            {'name': None,
            'characters_used': "['Meta Knight', 'Meta Knight', 'Meta Knight']",
            'wins': 5},
            {'name': 'Eason',
            'characters_used': "['Cloud', 'Joker', 'Mario', 'Link', 'Meta Knight']",
            'wins': 4}]
        pass
