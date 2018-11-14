class Animal:
    def __init__(self, name):
        self.name = name
        self.health = 50
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print(self.health)
        return self

animal1 = Animal("animal1")

animal1.walk().walk().walk().run().run().displayHealth()
# Output --> 37

class Dog(Animal):
    def __init__(self):
        super().__init__(self)
        self.health = 150
    def pet(self):
        self.health += 5
        return self

dog = Dog()

dog.walk().walk().walk().run().run().pet().displayHealth()
# Output --> 142

class Dragon(Animal):
    def __init__(self):
        super().__init__(self)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        super().displayHealth()
        print("I am a Dragon")

dragon = Dragon()

dragon.walk().fly().displayHealth()
# Output --> 159
#           I am a Dragon

animal2 = Animal("animal2")

animal2.pet().fly()
# error

animal2.displayHealth()
# 50 

dog.fly()
# error
