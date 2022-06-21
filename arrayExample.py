from array import *

arr = array('i',[])

n = int(input("Enter length of an array"))

for i in range(n):
    x = int(input("enter next element"))
    arr.append(x)

print(arr)

