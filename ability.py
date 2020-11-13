import random

class Ability():
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        random_dmg = random.randint(0, self.max_damage)
        return random_dmg

ability_name = Ability("test ability", 200)
print(ability_name.name)
print(ability_name.attack())