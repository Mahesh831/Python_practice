numbers = [12,10,9,44,88]
#print(min(numbers),max(numbers))
'''numbers.sort()
print(numbers[0],numbers[-1])'''
small = numbers[0]
large = numbers[0]
length = len(numbers)
for i in range(1,length):
    if small > numbers[i]:
        small = numbers[i]
    if large < numbers[i]:
        large = numbers[i]
print(small,large)
