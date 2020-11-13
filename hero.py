import random
from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, starting_health = 100):
        self.name = name
        self.starting_health = starting_health
        self.current_health =  starting_health
        self.abilities = list()
        self.armors = list()

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):
        total_dmg = 0
        for ability in self.abilities:
            total_dmg += ability.attack()
        
        return total_dmg

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
                    print('running loop again')

                print('exited while loop')
                if self.is_alive() == True:
                    print(f'{self.name} won')
                elif opponent.is_alive() == True:
                    print(f'{opponent.name} won')
                else:
                    print("'Both of ya'll died... somehow")

# Initialize hero 1
hero1 = Hero("Bob", 900)

# Initialize hero 2
hero2 = Hero("Tom", 900)

# Create abilities for hero 1 and add them to the list
ability = Ability("Great debugging", 50)
ability2 = Ability("Lesser debugging", 10)
hero1.add_ability(ability)
hero1.add_ability(ability2)

# Create armors for hero 1 and add them to the list
armor = Armor("Stone Helmet", 10)
armor2 = Armor("Stone Carapace", 20)
hero1.add_armor(armor)
hero1.add_armor(armor2)

# Create abilities for hero 2 and add them to the list
ability3 = Ability("Great debugging", 50)
ability4 = Ability("Lesser debugging", 10)
hero2.add_ability(ability3)
hero2.add_ability(ability4)

# Create armors for hero 2 and add them to the list
armor3 = Armor("Stone Helmet", 10)
armor4 = Armor("Stone Carapace", 20)
hero2.add_armor(armor3)
hero2.add_armor(armor4)

hero1.fight(hero2)