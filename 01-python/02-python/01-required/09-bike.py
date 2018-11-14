class Bike:
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print(self.price, self.max_speed, self.miles)
        return self
    def ride(self):
        print("Riding")
        self.miles += 10
        return self
    def reverse(self):
        print("Reversing")
        self.miles -= 5
        return self

bike1 = Bike(200, "25mph")
bike2 = Bike(200, "25mph")
bike3 = Bike(200, "25mph")

bike1.ride().ride().ride().reverse().displayInfo()

bike2.ride().ride().reverse().reverse().displayInfo()

bike3.reverse().reverse().reverse().displayInfo()

## What would you do to prevent the instance from having negative miles?
# In the displayInfo method, you can have it print absolute value of self.miles by using abs() function as follows:

#   def displayInfo(self):
#       print(self.price, self.max_speed, abs(self.miles))
#       return self

## Which methods can return self in order to allow chaining methods?
#   displayInfo(), ride(), and reverse() can all return self and thus allow chaining methods
    