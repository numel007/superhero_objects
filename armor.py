import random

class Armor():
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        random_def = random.randint(0, self.max_block)
        return random_def

armor_name = Armor("test armor", 100)
print(armor_name.name)
print(armor_name.block())