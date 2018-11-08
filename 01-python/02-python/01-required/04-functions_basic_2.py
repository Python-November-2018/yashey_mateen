#1. Countdown - Create a function that accepts a number as an input.  Return a new array that counts down by one, from the number (as arrays 'zero'th element) down to 0 (as the last element).  For example countDown(5) should return [5,4,3,2,1,0].

def countdown(x): 
...   newArr=[] 
...   for x in range(x, 0, -1): 
...     newArr.append(x) 
...   return newArr 
...   
>>> countdown(5)


#2. Print and Return - Your function will receive an array with two numbers. Print the first value, and return the second.
def printreturn(x,y):
    print x
    return 


#3. First Plus Length - Given an array, return the sum of the first value in the array, plus the array's length.

def firstpluslength(x):
    return x[0] + len(x)


#4. Values Greater than Second - Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value.  Print how many values this is.  If the array is only one element long, have the function return False

def greaterthansecond(arr):
    arr2=[]
    if len(arr) == 0:
        return False
    for x in arr:
        if arr[x] > arr[1]:
            arr2.append(arr[x])
    print(arr2)
    print(len(arr2))


#5. This Length, That Value - Write a function called lengthAndValue which accepts two parameters, size and value. This function should take two numbers and return a list of length size containing only the number in value. For example, lengthAndValue(4,7) should return [7,7,7,7].

def lengthAndValue(this, that):
    arr=[]
    for x in range (0, this):
        arr.append(that)
    return arr
