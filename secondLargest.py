numbers = [10,5,7,9,22,4]
#print(numbers[-2])
fm = max(numbers[0],numbers[1])
sm = max(numbers[0],numbers[1])
length = len(numbers)
for i in range(2,length):
    if numbers[i]>fm:
        sm = fm
        fm = numbers[i]
    elif numbers[i]>sm: 
        sm = numbers[i]
print(sm)
    