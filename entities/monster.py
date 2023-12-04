# entities/player.py

class Monster:
    def __init__(self, name, desc, weight, health, fight):
        self.name = name
        self.desc = desc
        self.weight = weight
        self.health = health
        self.fight = fight

    def __str__(self):
        return self.name

# Rest of the code remains the same
