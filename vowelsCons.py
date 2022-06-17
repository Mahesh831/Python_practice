#no of vowels and consonants
name = input('Enter name ')
vowelsList = ['a','e','i','o','u']
vowelsCount = 0
consonantsCount = 0
for i in name:
    if i in vowelsList:
        vowelsCount = vowelsCount + 1
    else:
        consonantsCount = consonantsCount + 1
print('Number of vowels {}, Number of Consonants {}'.format(vowelsCount,consonantsCount))