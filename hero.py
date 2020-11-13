import random
from ability import Ability
from armor import Armor
from weapon import Weapon


class Hero:
    def __init__(self, name, starting_health = 100):
        self.name = name
        self.starting_health = starting_health
        self.current_health =  starting_health
        self.abilities = list()
        self.armors = list()
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def attack(self):
        total_dmg = 0
        for ability in self.abilities:
            total_dmg += ability.attack()
        
        return total_dmg

    def add_kill(self, num_kills):
        self.kills += num_kills
        return self.kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths
        return self.deaths

    def defend(self, damage_amt):
        total_armor = 0
        for armor in self.armors:
            total_armor += armor.block()

        return damage_amt - total_armor

    def take_damage(self, damage):
        self.current_health -= self.defend(damage)
        return self.current_health

    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False

    def fight(self, opponent):
            if len(self.abilities) == 0 and len(opponent.abilities) == 0:
                print("Draw")
            else:
                while self.is_alive() == True and opponent.is_alive() == True:
                    opponent.take_damage(self.attack())
                    self.take_damage(opponent.attack())

                if self.is_alive() == True:
                    self.add_kill(1)
                    opponent.add_death(1)
                    print(f'{self.name} won')
                elif opponent.is_alive() == True:
                    opponent.add_kill(1)
                    self.add_death(1)
                    print(f'{opponent.name} won')
                else:
                    self.add_death(1)
                    opponent.add_death(1)
                    print("'Both of ya'll died... somehow")