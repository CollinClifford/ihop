# dungeon/dungeon.py
from random import shuffle
from room import Room

class Dungeon:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        """Add a room to the dungeon."""
        self.rooms.append(room)

    def shuffle_rooms(self):
        """Shuffle the order of rooms."""
        shuffle(self.rooms)
