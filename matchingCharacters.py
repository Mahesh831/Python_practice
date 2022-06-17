#matching characters from a sring
name = "mahesh"
matchingCharacters = set()
for i in name:
	if name.count(i)>1:
		matchingCharacters.add(i)
print(matchingCharacters)