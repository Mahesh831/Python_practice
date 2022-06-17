#filter
def isEven(num):
    return num%2==0
numbers = [10,11,23,22,80,87]
result = filter(isEven,numbers)
print(list(result))


#use anonymous fuction insted of isEven
numbers = [10,11,23,22,80,87]
result = filter(lambda num:num%2==0,numbers)
print(list(result))


#map 
friends = ['jenny','marry','loggy']
result = map(lambda name:name.upper(),friends)
print(list(result))

#reduc3
from functools import reduce
def addAll(a,b):
    return a+b
numbers = [20,1,3,10,5]
result = reduce(addAll,numbers) #without intial
#result = reduce(addAll,numbers,10)  #with intial value
print(result)

####lambda
numbers = [20,1,3,10,5]
result = reduce(lambda a,b:a+b,numbers,10)
print(result)

