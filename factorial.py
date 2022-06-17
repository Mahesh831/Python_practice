n = int(input('enter n value '))
if n<0:
    print('Invalid number, please enter a valid number')
elif n==0:
    print('factorial of 0 is 1')
else:
    factorial = 1
    for i in range (1,n+1):
        factorial = factorial * i
    print('foctorial of a {} is {}'.format(n,factorial))