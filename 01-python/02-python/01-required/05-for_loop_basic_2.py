#1. Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big". Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].
def makeItBig(arr):
  newarr=[]
  biggie = 'big'
  for i in range(0, len(arr), +1):
    if arr[i]<0:
      newarr.append(arr[i])
    if arr[i]>0:
      arr[i] = biggie
      newarr.append(arr[i])
  print(newarr)

makeItBig([-1, 3, 5, -5])


#2. Count Positives - Given an array of numbers, create a function to replace last value with number of positive values. Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).
def countPositives(arr):
    positiveCount = 0
    for i in range(0, len(arr), +1):
        if arr[i]>0:
            positiveCount+=1
        arr[len(arr)-1]=positiveCount
    print(arr)

countPositives([-1,1,1,1])


#3. SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array.  For example sumTotal([1,2,3,4]) should return 10
def sumTotal(arr):
    sum = 0
    for i in range(0, len(arr), +1):
        sum+=arr[i]
    print(sum)

sumTotal([1,2,3,4])



#4. Average - Create a function that takes an array as an argument and returns the average of all the values in the array.  For example multiples([1,2,3,4]) should return 2.5
def multiples(arr):
    sum = 0
    for i in range(0, len(arr), +1):
        sum+=arr[i]
    avg = sum/len(arr)
    print(avg)

multiples([1,2,3,4])

#5. Length - Create a function that takes an array as an argument and returns the length of the array.  For example length([1,2,3,4]) should return 4
def length(arr):
    print(len(arr))

length([1,2,3,4])



#6. Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.  If the passed array is empty, have the function return false.  For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.
def minimum(arr):
    min = arr[0]
    if(len(arr) == 0):
        return false
    for i in range(0, len(arr), +1):
        if(arr[i]<min):
            min = arr[i]
    print(min)

minimum([1,2,3,4])
minimum([-1,-2,-3])
    

#7. Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.  If the passed array is empty, have the function return false.  For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.
def maximum(arr):
    max = arr[0]
    if(len(arr) == 0):
        return false
    for i in range(0, len(arr), +1):
        if(arr[i]>max):
            max= arr[i]
    print(max)

maximum([1,2,3,4])
maximum([-1,-2,-3])


#8. UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.
def ultimateAnalyze(arr):
    ultimate = []
    min = arr[0]
    max = arr[0]
    sum = 0
    for i in range(0, len(arr), +1):
        sum+=arr[i]
    avg = sum/len(arr)
    ultimate.append(sum)
    ultimate.append(avg)
    for i in range(0, len(arr), +1):
        if(arr[i]<min):
            min = arr[i]
    ultimate.append(min)
    for i in range(0, len(arr), +1):
        if(arr[i]>max):
            max= arr[i]
    ultimate.append(max)
    ultimate.append(len(arr))
    print(ultimate)

ultimateAnalyze([1,2,3,4,5])

    
#9. ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.  Do this without creating an empty temporary array.  For example reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.
def reverse(arr):
    i = 0
    j = len(arr)-1
    for i in range (0, j, +1):
        arr[j], arr[i] = arr[i], arr[j]
        j-=1
        arr[i], arr[j] = arr[j], arr[i]
    print(arr)

reverse([1,2,3,4])
