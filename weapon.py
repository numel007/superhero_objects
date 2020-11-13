from ability import Ability
import random

class Weapon(Ability):
    def __init__(self, name, max_damage):
        super().__init__(name, max_damage)

    def attack(self):
        half_dmg = self.max_damage // 2
        random_half_dmg = random.randint(half_dmg, self.max_damage)
        return random_half_dmg