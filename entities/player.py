class Player:
    def __init__(self, name, password, max_weight_capacity=50):
        self.name = name
        self.password = password
        self.level = 1
        self.xp = 0
        self.next_level_threshold = 100  # XP required to level up
        self.inventory = []
        self.tickets = []
        self.max_weight_capacity = max_weight_capacity
        self.current_weight = 0
        self.health = 100
        self.fight = 10

    def list_inv(self):
        if len(self.inventory) > 0:
            print("On your person you have:")
            for item in self.inventory:
                print(item)
        else:
            print("You are currently carrying nothing.")

    def list_health(self):
        print(f"""
Health: {self.health}
Strength: {self.fight}

""")
        
    def list_xp(self):
        print(f"""
Level: {self.level}
Experience: {self.xp}
""")

    def __str__(self):
        return f"{self.name} (Level {self.level}, XP: {self.xp}, Health: {self.health}, Inventory: {self.inventory}, Weight: {self.current_weight}/{self.max_weight_capacity}, Strength: {self.fight})"

    def pick_up_item(self, item):
        """Add an item to the player's inventory."""
        if self.current_weight + item.weight > self.max_weight_capacity:
            print(f"{self.name}'s inventory is full. Cannot pick up {item}.")
        else:
            self.inventory.append(item)
            self.current_weight += item.weight
            print(f"{self.name} picked up {item}.")
            # self.gain_experience(10)  # Example: Gain XP for picking up an item

    def take_ticket(self, item):
        """Add an item to the player's inventory."""
        self.tickets.append(item)
        # self.current_weight += item.weight
        print(f"{self.name} picked up {item}.")
        # self.gain_experience(10)  # Example: Gain XP for picking up an item

    def use_item(self, item):
        """Use an item from the player's inventory."""
        if item in self.inventory:
            if item.disposable:
                self.inventory.remove(item)
                self.current_weight -= item.weight
                self.health += item.health
                print(f"{self.name} used {item}.")
            else:
                print(f"{self.name} equiped {item}!")
                self.fight += item.fight
                # self.gain_experience(20)  # Example: Gain more XP for using a reusable item
        else:
            print(f"{self.name} doesn't have {item} in the inventory.")

    def take_damage(self, damage):
        """Reduce player's health by the specified amount."""
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

    def gain_experience(self, xp):
        """Gain experience points and check for level-up."""
        self.xp += xp
        print(f"{self.name} gained {xp} XP.")
        if self.xp >= self.next_level_threshold:
            self.level_up()

    def level_up(self):
        """Level up the player."""
        self.level += 1
        self.next_level_threshold *= 2  # Example: Doubling XP required for the next level
        self.health = 100  # Example: Reset health upon leveling up
        print(f"{self.name} leveled up to Level {self.level}!")

    def cook_for_quest(self, quest_item, quest_ingredient):
        """Cook quest items to fulfill a quest."""
        if quest_item in self.inventory and quest_ingredient in self.inventory:
            # Check if the player has enough of the required ingredients
            required_quantity = quest_item.quantity
            actual_quantity = min(self.inventory.count(quest_item), self.inventory.count(quest_ingredient))

            if actual_quantity >= required_quantity:
                # Fulfill the quest
                self.inventory.remove(quest_item)  # Remove quest item
                self.inventory.remove(quest_ingredient)  # Remove quest ingredient
                self.current_weight -= quest_item.weight + quest_ingredient.weight

                # Example: Gain XP for completing the quest
                xp_earned = 50  # Adjust as needed
                self.gain_experience(xp_earned)

                print(f"{self.name} cooked {required_quantity} {quest_item} with {required_quantity} {quest_ingredient} and fulfilled the quest!")
            else:
                print(f"{self.name} doesn't have enough required ingredients to fulfill the quest.")
        else:
            print(f"{self.name} is missing quest items in the inventory.")

    def inspect_quest_item(self, quest_item):
        """Inspect a quest item in the player's inventory."""
        if quest_item in self.inventory:
            print(f"{self.name} inspects {quest_item}: {quest_item.description}")
        else:
            print(f"{self.name} doesn't have {quest_item} in the inventory.")
    
    def read_ticket(self, ticket):
        """Reads the ticket for the quest"""
        if ticket in self.tickets:
            print(f"""{self.name} reads the ticket:
{ticket.name}
{ticket.desc}
{ticket.ingredients}""")
