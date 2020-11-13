class Animal():
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"

    def drink(self):
        return f"{self.name} is drinking"


class Frog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def jump(self):
        return f"{self.name} is jumping"


dog = Animal("Doggo")
frog = Frog("Froggo")
print(frog.eat())
print(frog.drink())
print(frog.jump())