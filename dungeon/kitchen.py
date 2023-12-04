
import json
from entities.player import Player
from entities.ingredient import Ingredient
from entities.item import Item
from entities.monster import Monster
from entities.ticket import Ticket

# Ingredients
rat_corpse = Ingredient(name="Rat Corpse", weight=1, disposable=True)
tomato = Ingredient(name="Rotten Tomato", weight=1, disposable=True)

# Weapons
frying_pan = Item(name="Frying Pan", weight=5, health=0, fight=5, disposable=False)
butcher_knife = Item(name="Butcher Knife", weight=2, health=0, fight=5, disposable=False)
spatula = Item(name="Spatula", weight=1, health=0, fight=1, disposable=False)

# Potions
orange_soda = Item(name="Orange Soda", weight=1, health=5, fight=0, disposable=True)
grape_soda = Item(name="Grape Soda", weight=1, health=1, fight=0, disposable=True)
moldy_bread = Item(name="Moldy Bread", weight=1, health=5, fight=0, disposable=True)

# Monsters
rat = Monster(name="Rat", desc="A rabid rat with beady eyes", weight=1, health=10, fight=1)

# Tickets
ticket_1 = Ticket(name="Rattatouille", desc="A gruesome delight, melding rat corpses with succulent tomatoes", ingredients=["Rat Corpse","Rat Corpse","Rat Corpse","Rotten Tomato"])

kitchen_json = [
    {
        "id": 1,
        "name": "Back Alley",
        "desc": "A dimly lit area with a dumpster and a back exit to the main road.", 
        "items": [rat_corpse],
        "options": [
            {
                "name": "Exit",
                "direction": "West",
                "nextId": "null"
            },
            {
                "name": "Pantry",
                "direction": "South",
                "nextId": 2
            }
        ]
     },
     {
        "id": 2,
        "name": "Dish Pit",
        "desc": "Stacks of dirty dishes and a foul smell.", 
        "items": [],
        "options": [
            {
                "name": "Back Alley",
                "direction": "North",
                "nextId": 1
            },
            {
                "name": "Prep Area",
                "direction": "West",
                "nextId": 3
            }
        ]
     },
     {
        "id": 3,
        "name": "Prep Area",
        "desc": "Dirty cutting boards and half carved carcasses.", 
        "items": [moldy_bread, butcher_knife],
        "options": [
            {
                "name": "Dish Pit",
                "direction": "East",
                "nextId": 2
            },
            {
                "name": "Make Line",
                "direction": "South",
                "nextId": 4
            },
            {
                "name": "Pantry",
                "direction": "West",
                "nextId": 5
            }
        ]
     },
     {
        "id": 4,
        "name": "Make Line",
        "desc": "Cooking stations bustling with activity.", 
        "items": [frying_pan],
        "options": [
            {
                "name": "Prep Area",
                "direction": "North",
                "nextId": 3
            },
            {
                "name": "Order Window",
                "direction": "West",
                "nextId": 6
            }
        ]
     },
     {
        "id": 5,
        "name": "Pantry",
        "desc": "Shelves stocked with mysterious ingredients. The door leads to the dungeon.", 
        "items": [tomato],
        "options": [
            {
                "name": "Prep Area",
                "direction": "East",
                "nextId": 3
            },
            {
                "name": "Order Window",
                "direction": "South",
                "nextId": 6
            },
            {
                "name": "Dungeon",
                "direction": "Down",
                "nextId": "null"
            }
        ]
     },
     {
        "id": 6,
        "name": "Order Window",
        "desc": "A window to serve completed dishes.", 
        "items": [ticket_1],
        "options": [
            {
                "name": "Pantry",
                "direction": "North",
                "nextId": 5
            },
            {
                "name": "Dining Room",
                "direction": "South",
                "nextId": 7
            },
            {
                "name": "Make Line",
                "direction": "East",
                "nextId": 4
            }
        ]
     },
     {
        "id": 7,
        "name": "Dining Area",
        "desc": "Long tables and chairs scattered about.",
        "items": [orange_soda],
        "options": [
            {
                "name": "Order Window",
                "direction": "North",
                "nextId": 6
            }
        ]
     }
]

def get_valid_directions(current_room_id, kitchen):
    """Get valid directions for the current room."""
    current_room = next(room for room in kitchen if room["id"] == current_room_id)
    return [option["direction"] for option in current_room['options']]

def navigate_kitchen(current_room_id, kitchen, char):
    """Navigate the kitchen."""

    while True:
        current_room = next(room for room in kitchen if room["id"] == current_room_id)
        def show_room():
            print(f"{current_room['name']}")
            print(f"{current_room['desc']}")
            if len(current_room["items"]) > 0:
                print("The following items are in this room")
                for item in current_room['items']:
                    print(item)
            valid_directions = get_valid_directions(current_room_id, kitchen)
            print("Directions:", valid_directions)
        
        valid_directions = get_valid_directions(current_room_id, kitchen)
        # print("Directions:", valid_directions)
        show_room()
        user_input = input().strip().upper()

        if user_input.lower() == "s" or user_input.lower() == "south":
            user_input = "South"
        elif user_input.lower() == "n" or user_input.lower() == "north":
            user_input = "North"
        elif user_input.lower() == "e" or user_input.lower() == "east":
            user_input = "East"
        elif user_input.lower() == "w" or user_input.lower() == "west":
            user_input = "West" 
        elif user_input.lower() == "d" or user_input.lower() == "down":
            user_input = "Down"

        if user_input.lower() == "inventory":
            char.list_inv()
        elif user_input.lower() == "stats":
            char.list_health()
        elif user_input.lower() == "experience":
            char.list_xp()
        elif user_input.lower() == "look":
            show_room()
        elif user_input in valid_directions:
            option = next((opt for opt in current_room['options'] if opt["direction"].upper() == user_input.upper()), None)
            if option:
                next_room_id = option["nextId"]
                if user_input.lower() == 'd' and current_room_id == 5:
                    print("Descending into the dungeon...")
                    # Call your Dungeon function here
                    break
                else:
                    current_room_id = next_room_id
            else:
                print("Invalid command. Try again.")
        else:
            print("Invalid command. Try again.")
    
    return current_room_id