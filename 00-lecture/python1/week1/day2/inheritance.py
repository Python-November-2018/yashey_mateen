# file vehicles.py
class Vehicle:
    def __init__(self, wheels, capacity, make, model):
        self.wheels = wheels
        self.capacity = capacity
        self.make = make
        self.model = model
        self.mileage = 0
    def drive(self,miles):
        self.mileage += miles
        return self
    def reverse(self,miles):
        self.mileage -= miles
        return self
# Make the following classes that inherit from Vehicle --> Implicit Inheritance
    # Implicit Inheritance - allows us to use inherited attributes and methods of the Vehicle(parent) class in our new subclasses
class Bike(Vehicle):
    def vehicle_type(self):
        return "Bike"
class Car(Vehicle):
    def set_wheels(self):
        self.wheels = 4
        return self
class Airplane(Vehicle):
    def fly(self, miles):
        self.mileage += miles
        return self
v = Vehicle(4,8,"dodge","minivan")
print(v.make)
b = Bike(2,1,"Schwinn","Paramount")
print(b.vehicle_type())
c = Car(8,5,"Toyota", "Matrix")
c.set_wheels()
print(c.wheels)
a = Airplane(22,853,"Airbus","A380")
a.fly(580)
print(a.mileage)


# General skeleton for Implicit Inheritance:
class Parent:
  # parent methods and attributes here
class Child(Parent): #inherits from Parent class so we define Parent as the first parameter
  # parent methods and attributes are implicitly inherited
  # child methods and attributes

# Super - to reference a method in parent class if we want to customize it.
    # we call it by super and change just one attribute, rather than overwriting completely

class Human:
    def __init__(self):
        self.health = 5
        self.intelligence = 3
        self.strength = 2
        self.stealth = 1

class Wizard(Human):
    def __init__(self):
        super().__init__(self) # use super to call the Human __init__() method
        self.intelligence = 10 # every wizard starts off with 10 intelligence, overwriting the 3 from Human
    def heal(self):
        self.health += 10 # all wizards also get a heal() method
class Ninja(Human):
    def __init__(self):
        super().__init__(self) # use super to call the Human __init__() method
        self.stealth = 10 # every Ninja starts off with 10 stealth, overwriting the stealth of 1 from Human
    def steal(self):
        self.stealth += 5 # all ninjas also get a steal() method
class Samurai(Human):
    def __init__(self):
        super().__init__(self) # use super to call the Human __init__() method
        self.strength = 10 # every Samurai starts off with 10 strength, overwriting the 2 from Human
    def sacrifice(self):
        self.health -= 5 # all samurais also get a sacrifice() method

