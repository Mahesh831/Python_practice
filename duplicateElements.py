numbers = [1,2,3,3,5,8,2]
newNumbers = []
for i in numbers:
    if i not in newNumbers:
        newNumbers.append(i)
print('after removing duplicate elements',newNumbers)
        