class Bottle:
    #properties/state
    '''id = 1
    color = "red"
    capacity = 1
    height = 10'''
    #static/class variable
    companyName = "Sirpa"
    #constructor
    def __init__(self,color,capacity):
        self.color=color
        self.capacity=capacity
        print('constructer')
    #destructor
    '''def __del__(self):
        print('destructor')'''
    #behavior/functions
    def wash(self):
        print(self)
        print('washing')
    def setCap():
        print('seting Cap')
    def fillWater():
        print('filling water')
print(Bottle.companyName) #calling static variable
bottle1 = Bottle("green",1)
bottle2 = Bottle("red",2)
bottle3 = Bottle("blue",3)
print(bottle1.color)
print(bottle2.capacity)
print(bottle3.color)
bottle1.wash()
print(bottle1.companyName)   #calling instance variable

#INHERITENCE
#creating child class 
print("=========child class creatoion ")
class copperBottle(Bottle):
    def __init__(self):
        print('child Constructer')
    def morningWater():
        print('morning water')
print(copperBottle.companyName)
copper1 = copperBottle()
copper1.wash()