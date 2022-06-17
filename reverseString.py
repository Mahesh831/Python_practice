n = input('enter a string')
print('entered string',n)
    
#print(n[::-1]) # using slice method [start:end:step]
#another logic using for loop
reverse =""
for i in n:
    reverse = i+reverse
print(reverse)