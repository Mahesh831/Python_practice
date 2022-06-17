name = input('enter name')
foundNonRepeated = False
for i in name:
    if name.count(i)==1:
        foundNonRepeated = True
        print(i)
        break
if foundNonRepeated == False:
    print('no non repeatd charaacters found')