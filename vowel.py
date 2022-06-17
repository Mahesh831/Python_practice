name = input('Enter your Name')
vowelsList = ['a','e','i','o','u']
for character in name:
    if character in vowelsList:
        print(character,'-it is vowel')
    else:
        print(character,'-it is consonant')