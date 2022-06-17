#write
'''file = open('maheshroman.txt','w')
#write(data)
#file.write('hi ra')
#writelines()
friendsList = ["nandu","pranay","raju"]
file.writelines(friendsList)'''

#read
#file = open('maheshroman.txt','r')
#print(file.read())

#append
#file = open('maheshroman.txt','a')
#file.write('yela vunav')

##with statement
with open('maheshroman.txt','r') as file:
    print(file.read())