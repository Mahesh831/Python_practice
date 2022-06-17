n = int(input('Enter a number'))
originalValue = n
reverse = 0
while n>0:
    num = n%10
    reverse = reverse*10+num
    n = n//10
print('Reverse of a number {} is {}'.format(originalValue,reverse))