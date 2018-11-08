#lists and tuples work almost exactly the same except tuples are immutable - you can't update, create, or change anything once it is created 

#iterating through tuples is much faster than iterating through lists

list = [99,4,2,5,-3]
tuple = (99,4,2,5,-3)
print(list[:])
#the output would be [99,4,2,5,-3]
print(list[1:])
#the output would be [4,2,5,-3];
print(list[:4])
#the output would be [99,4,2,5]
print(list[2:4])
#the output would be [2,5];


Some built-in functions for sequences:

max(sequence) returns the largest value in the sequence
sum(sequence) return the sum of all values in sequence
map(function, sequence) applies the function to every item in the sequence you pass in. Returns a list of the results.
min(sequence) returns the lowest value in a sequence.
sorted(sequence) returns a sorted sequence


capitals = {"svk":"Bratislava","deu":"Berlin", "dnk":"Copenhagen"}
# creating a new key/value pair
capitals["abc"] = "New Country" 
# updating
capitals["abc"] = "ABC Country"
#to print all keys
for data in capitals:
     print(data)
#another way to print all keys
for key in capitals.keys():
     print(key)
#to print the values
for val in capitals.values():
     print(val)
#to print all keys and values
for key, val in capitals.items():
     print(key, " = ", val)

Built-in Functions and Methods for Dictionaries
Python includes the following standalone functions for dictionaries:

len() - give the total length of the dictionary.
str() - produces a string representation of a dictionary.
type() - returns the type of the passed variable. If passed variable is a dictionary, it will then return a dictionary type.
Python includes the following dictionary methods (either dict.method(yourDictionary) or yourDictionary.method() will work):

.clear() - removes all elements from the dictionary
.copy() - returns a shallow copy dictionary
.fromkeys(sequence, [value]) - create a new dictionary with keys from sequence and values set to value.
.get(key, default=None) - for key key, returns value or default if key is not in dictionary.
.items() - returns a view object of dictionary's (key, value) tuple pairs.
.keys() - return a view object of dictionary keys.
.pop(key) - returns the value associated with the key and removes the key-value pair from the dictionary.
.setdefault(key, default=None) - similar to get(), but will set dict[key]=default if key is not already in dictionary.
.update(dict2) - adds dictionary dict2's key-values pairs to an existing dictionary.
.values() - returns a view object of dictionary values.

