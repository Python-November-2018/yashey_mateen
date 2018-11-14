print("this is a sample string")


name = "Zen"
print("My name is", name)

name = "Zen"
print("My name is " + name)



# Literal string interpolation - With this method, we will produce f-strings, which are denoted by the 'f' we put before the string. The variables we would like to inject are placed in the string within curly brackets.
first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")



# String formatting - An older version of string interpolation uses the .format() method.
first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))


# %-formatting - As you read other people's code, you may see an even older method of string interpolation, so you should know about it:

# use %s as a placeholder for strings and %d as a placeholder for numbers
hw = "Hello %s" % "world" 
py = "I love Python %d" % 3 
print(hw, py)
# the output would be: Hello world I love Python 3
# we can also pass variables
name = "Zen"
age = 27
print("My name is %s and I'm %d" % (name, age))


# Built-In String Methods - String methods are functions that we can run on a string. We already showed you one above, the .format() method. Here's how to use these methods:
x = "hello world"
print(x.title())
# output:
"Hello World"

#commonly used string methods

string.upper(): returns a copy of the string with all the characters in uppercase.
string.lower(): returns a copy of the string with all the characters in lowercase.
string.count(substring): returns number of occurrences of substring in string.
string.split(char): returns a list of values where string is split at the given character. Without a parameter the default split is at every space.
string.find(substring): returns the index of the start of the first occurrence of substring within string.
string.isalnum(): returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return False for this method. Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans.
string.join(list): returns a string that is all strings within our set (in this case a list) concatenated.
string.endswith(substring): returns a boolean based upon whether the last characters of string match substring.