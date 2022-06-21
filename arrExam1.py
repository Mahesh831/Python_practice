from array import *

arr = array('i',[])

n = int(input("Enter length of an array"))

for i in range(n):
    x = int(input("enter next element"))
    arr.append(x)

print(arr)



val = int(input("enter val to search")

k = 0

for a in arr:   
    if a==val:
        print(k)
        break
    
    
    k+=1
    
    
print(arr.index(val))