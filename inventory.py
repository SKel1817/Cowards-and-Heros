#lists that contain all possible (maybe make dictionary for damage)
# or make each weapon a dictornary and have dictionary in list
weapons = []
potions = []
kits = []
items = []

#what the character has, can be added to by using class inventory
char_weap = []
char_pot = []
char_kit = []
char_items = []
class Inventory:
    def __int__(self, weapons, potions, kits, items):
        self.weapons = char_weap
        self.potions = char_pot
        self.kits = char_kit
        self.items = char_items
    def add_item(self):
        print("you have added an item")
    def lose_item(self):
        print("You lost an item")
    def list_inv(self):
        print("You have....")

class loot:
    def __int__(self, weapons, potions, kits, items):
        self.weapons = weapons
        self.potions = potions
        self.kits = kits
        self.items = items
    def list():
        print("You have found...")