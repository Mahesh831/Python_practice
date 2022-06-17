n = int(input('enter a number'))
originalValue = n
sum = 0
while n>0:
    num = n%10
    sum = sum + num**3
    n = n//10
print(sum)
if originalValue==sum:
    print('Armstrong')
else:
    print('Not Armstrong')