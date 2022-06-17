from array import *
int_arr = array("i",[])
x = int(input('Enter array length'))
for i in range(x):
    n = int(input('Enter elements'))
    int_arr.append(n)
print(int_arr)