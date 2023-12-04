from item import Item
from ingredient import Ingredient
from ticket import Ticket
from monster import Monster

# Tickets
ticket_1 = Ticket(name="Rattatouille", desc="A gruesome delight, melding rat corpses with succulent tomatoes", ingredients=["Rat Corpse","Rat Corpse","Rat Corpse","Rotten Tomato"])

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