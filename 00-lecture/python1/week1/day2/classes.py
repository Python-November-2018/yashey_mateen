# every class needs a constructor

# all methods are functions, but not all functions are methods

# self = reference to the object that invoked this function

class Human:
    def __init__(self, eye_col, name):
        self.eye_color = eye_col
        self.name = name
        self.health = 100

    def say_name(self):
        print('Hi, my name is' + self.name)
        return self



wes = Human('blue') # this Human is an object
print(wes.__dict__) # convert to dictionary format
jay = Human('brown', 'Jay')
wes = Human('blue', 'wes')
print(wes.__dict__)

print(wes.say_name())
# --> outputs: "Hi My name is Wes"
#               Wes

# here it will run the say_name function on 'wes' variable, so since function returns self, then 'wes' would be self

wes.workout().workout().workout().workout().workout()
wes.workout().display_health().workout().display_health()

User.objects.filter(first_name="Wes").exclude(last_name="Harper")


print(wes, name)
wes.say_name()


    def workout(self):
        self.health += 10
        return self
#every function in python returns something

print(wes.health)
wes.workout()
print(wes.health)


# Inheritance

# We take a class, and we want to augment that class with new information, we can use inheritance

class Ninja(Human):
    pass
# class Ninja has all the say properties and methods  of the Human class just by inheriting from it 

wes = Ninja


class Nerd(Human):
    # adding attributes
    def __init__(self, eye_col, name, favorite_book): #ovverride attributes of init from Human class
        super().__init__(eye_col, name) # super refers to the parent class, this line passes those parameters to Nerd class
        self.favorite_book = favorite_book

print(wes.favorite_book)
         




    def read(self):
        print('Deep in thoughts...')
        return self
    
wes = Nerd('blue', 'Wes')