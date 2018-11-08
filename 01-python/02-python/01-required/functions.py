def add(a,b):
    x=a+b
    return x
# the return value gets assigned to the "result" variable
result = add(3,5)
print(result) # this should print 8


#the following function has one parameter
def say_hi(name):
    print("Hi, " + name)

#invoking the function passing in one argument
say_hi('Michael')
say_hi('Anna')
say_hi('Eli')
# In the previous example, name is the parameter; 'Michael', 'Anna', & 'Eli' are arguments

# **A functional call is equal to whatever that function returns**

def say_hi(name):
    return "Hi " + name

greeting = say_hi("Michael") #the returned value from say_hi function gets assigned to the 'greeting' variable
print(greeting) # this will output 'Hi Michael'

def add(a, b):
    x = a + b
    return x
sum1 = add(4,6)
sum2 = add(1,4)
sum3 = sum1 + sum2

#Output: 10, 5, 15


