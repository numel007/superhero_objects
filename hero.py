import random

class Hero:
    def __init__(self, name, starting_health = 100):
        self.name = name
        self.starting_health = starting_health
        self.current_health =  starting_health

    def fight(self, opponent):
        """Pit 2 heroes against each other, choose a random winner"""
        heros = [self.name]
        heros.append(opponent.name)
        winner = random.choice(heros)
        print(winner)

my_hero = Hero("Bob", 400)
my_hero2 = Hero("Tom", 400)

my_hero.fight(my_hero2)