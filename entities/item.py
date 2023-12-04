# entities/player.py

class Item:
    def __init__(self, name, weight, health, fight, disposable=True):
        self.name = name
        self.weight = weight
        self.disposable = disposable
        self.health = health
        self.fight = fight

    def __str__(self):
        return self.name

# Rest of the code remains the same
