from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team


class Arena:
    def __init__(self):
        self.team_one = Team("team 1")
        self.team_two = Team("team 2")

    def create_ability(self):
        name = input("What is the ability name? ")
        max_damage = int(input("What is the max ability damage? "))

        return Ability(name, max_damage)

    def create_weapon(self):
        name = input("What is the weapon name? ")
        max_damage = int(input("What is the max weapon damage? "))

        return Weapon(name, max_damage)

    def create_armor(self):
        name = input("What is the armor name? ")
        max_reduction = int(input("What is the max armor reduction? "))

        return Armor(name, max_reduction)

    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input(
                "[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                # TODO add an ability to the hero
                # HINT: First create the ability, then add it to the hero
                hero.add_ability(self.create_ability())
            elif add_item == "2":
                # TODO add a weapon to the hero
                # HINT: First create the weapon, then add it to the hero
                hero.add_weapon(self.create_weapon())
            elif add_item == "3":
                # TODO add an armor to the hero
                # HINT: First create the armor, then add it to the hero
                hero.add_armor(self.create_armor())
        return hero

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    # Now implement build_team_two
    #HINT: If you get stuck, look at how build_team_one is implemented
    def build_team_two(self):
        '''Prompt the user to build team_two'''
        numOfTeamMembers = int(input("How many members in Team Two?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        # TODO: This method should battle the teams together.
        # Call the attack method that exists in your team objects
        # for that battle functionality.
        self.team_one.attack(self.team_two)

    def show_stats(self):
        print("\n")
        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")

        # This is how to calculate the average K/D for Team One
        team_kills = 0
        team_deaths = 0
        for hero in self.team_one.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_one.name + " average K/D was: " + str(team_kills/team_deaths))

        # TODO: Now display the average K/D for Team Two
        team_kills2 = 0
        team_deaths2 = 0
        for hero in self.team_two.heroes:
            team_kills2 += hero.kills
            team_deaths2 += hero.deaths
        if team_deaths2 == 0:
            team_deaths2 = 1
        print(self.team_two.name + " average K/D was: " + str(team_kills2/team_deaths2))

        # Here is a way to list the heroes from Team One that survived
        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_one.name + ": " + hero.name)

        #TODO: Now list the heroes from Team Two that survived
        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_two.name + ": " + hero.name)

arena = Arena()
arena.build_team_one()
arena.build_team_two()
arena.team_battle()
arena.show_stats()