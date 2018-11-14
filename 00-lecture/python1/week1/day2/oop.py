# object oriented programming

# class = blueprint of what I want to do, has 2 categories:
    #attributes - what it can have, variables inside a class 
        # characteristics shared by all instances of the class type. Variables stored within an object
    #methods - what it can do, functions inside a class
        # actions that an object can perform. functions that belong to a class. Some instructions that will only work when called on an object that has been created from that class. 


    #instances - objects created (instace/objects same thing)
        #instance attributes/instance methods - independent

        #public/private - you can create attributes that are private    

        # objects have two important features
            # storage of information 
            # ability to execute some logic 

        # objects can store two different types of information
            # attributes
            # methods 
    
    #constructor = methods that the program will run whenever you construct an new instance 

    #inheritance - class can inherit all attributes/methods of the parent class

    #self - When we call methods we do not have to pass in any arguments. this is known as implicit passage of self. We can now change the state of the single object by making modifications only to self. 
        # This parameter includes all the information about the individual object that has called the method. 

class User:
    # the __init__ method is called every time a new object is created 
    def __init__(self, name, email):
        # set some instance variables. just like any variable we can call these anything. Here we set some values that belong to each object to be equal to the values we passed in: self.email = email, etc
        self.name = name
        self.email = email
        self.logged = True
    # this is a method we created to help a user login. This method prints a string
    # login method changes the logged status for a single instance (the instance calling the method)
    def login(self):
        self.logged = True
        print(self.name + " is logged in.")
        # return self returns its own instance allowing you to chain methods after calling that method 
        return self
    # logout method changes the logged status for a single instance (the instance calling the method)
    def logout(self):
        self.logged = False
        print(self.name + " is not logged in.")
        return self
    # print name and email of the calling instance 
    def show(self):
        print(f"My name is {self.name}. You can email me at {self.email}.")
        return self


# We create a new instance by using the class name as if it were a function.

michael = User()
anna = User()

# now create an instance of the class
new_user = User("Anna", "anna@anna.com")
print(new_user.email)



# Chaining Mehotds
    # instead of...
        # user1.login()
        # user1.show()
        # user1.logout()
    # we could do this:
        # user1.login().show().logout()
    



