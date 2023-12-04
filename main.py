from entities.player import Player
from dungeon.room import Room
from dungeon.kitchen import navigate_kitchen, kitchen_json
import json

gobby = Player(name="Gobby", password="")

def game():
    # Load kitchen from JSON
    while True:


        kitchen = json.loads(kitchen_json)
        current_room_id = 1
        
        # Navigate the kitchens

        current_room_id = navigate_kitchen(current_room_id, kitchen, gobby)

if __name__ == "__main__":
    game()