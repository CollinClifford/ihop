class Room:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
        self.items = []

    def __str__(self):
        return f"{self.name}: {self.description}"