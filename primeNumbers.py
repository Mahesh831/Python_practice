#prime numbers from 1 t0 100
n = 100
#to get no of prime numbers
primeNumbers = []
for i in range(2,n+1):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)
        #primeNumbers.append(i)
#print('no of prime nos is',len(primeNumbers))