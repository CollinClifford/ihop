class Ingredient:
    def __init__(self, name, weight, disposable=True):
        self.name = name
        self.weight = weight
        self.disposable = disposable

    def __str__(self):
        return self.name