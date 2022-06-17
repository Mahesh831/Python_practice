#count of particularcharacter in a string
name = input('Enter name')
character = input('enter a character')
#print(name.count(character))
count = 0
for i in name:
    if character == i:
        count = count + 1
print('Count of a particular character {}'.format(count))