#sum of 1 to n program
n = int(input('enter a n value'))
sum = 0
for i in range(1,n+1):
	sum = sum+i
print('sum of 1 to {} is {}'.format(n,sum))