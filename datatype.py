#datatypes
"""marks = 500
percentage = (marks/600)*100
print(percentage)
channelName = "Mahesh Roman"
print(channelName)
#indexing
print(channelName[8])
print(channelName[-8])
#slicing
print(channelName[1:4])
print(channelName[5:10:2])
print(channelName[:4])
print(channelName[::-1])
cN = "maheshroman"+"naresh"
print(cN)
cnl = "maheshroman"*3
print(cnl)
channelNames = "mahesh is handsome"
print("handsome" in  channelNames)
print("handsome" not in  channelNames)
print("smart" in  channelNames)"""

#LIST
marks = [90,70,80,80,80,90,"10th marks"]
print(type(marks))
print(marks)
print("marks lenght",len(marks))
#nested list
biodata = [22,6303756423,"sklm",marks]
print(biodata)
#accessing listprint
print('second subject marks',marks[1])
print('lstsublmarks', marks[-1])
#accessing nested list
print(biodata[3][2])
#chnging or udateing list items
marks[1]=55
print(marks)
print(marks+biodata)
print(biodata*2)
#adding items to the list
#single item
marks.append(65)
print(marks)
#multiple items
marks.extend([85,"ssc marks"])
print(marks)
#adding at specific position
marks.insert(1,95)
print(marks)
#adding multiple items USING SLICING
marks[1:1] = ["my marks",70,80,90]
print(marks)
#DELETE AN ITEM FROM LIST
del marks[1]
print(marks)
#del marks
del marks[1:3]
print(marks)
#remove
print(marks.remove("10th marks"))
print(marks)
print(marks.pop(3))
print(marks)
print(marks.pop())
print(marks)

#SET
print("=====SET====")
anchors = {"sudheer","omkar","udhayabhanu","suma"}
print(type(anchors))
print(anchors)
#creating empty set
emptySet = set()
print(emptySet)
#ading single (add) adn multiple (update)
anchors.add("mahesh")
print(anchors)
anchors.update(["suresh","ramesh","rajesh"])
print(anchors)
anchors.discard("mahesh")
print(anchors)
anchors.remove("suma")
print(anchors)
print(anchors.pop())
anchors.clear()
print(anchors)


#dictionary
print("@@@@@4$$$$ DICTIONARY@@@@@4555")
bioData = {"name":"Mahesh","number":6303756423,"address":"srikakulam"}
print(type(bioData))
information = {"channel":"Subscribed","info":bioData}
print(information)
#ACCESSING
print(information["channel"])
print(information.get("channel"))
#adding or updating
information["channel"] = "maheshroman"
information["subscribed"] = True
print(information)
print(information)
#remove
del information["subscribed"]
print(information)
print(bioData.pop("name"))
print(bioData.popitem())