name = input('Enter name ')
foundNonRepeated = False
while name != "":
    originalLen = len(name)
    char = name[0]
    name = name.replace(char,'')
    replaceLen = len(name)
    if originalLen-1 == replaceLen:
        print('first non-repeated character is ',char)
        foundNonRepeated = True
        break
if foundNonRepeated == False:
    print('no non repeated characters found')