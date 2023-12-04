class Ticket:
    def __init__(self, name, desc, ingredients, xp):
        self.name = name
        self.desc = desc
        self.ingredients = ingredients
        self.xp = xp

    def __str__(self):
        return self.name