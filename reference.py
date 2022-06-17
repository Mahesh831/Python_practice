def reference(myMarks):
    myMarks[2] = 88   #here no break occur b/w paassed and received parameter
marks = [22,33,44,55]
reference(marks)
print(marks)

def calculate(myScore):
    myScore = [11,22,33] #here break occurs because values changes
score = [10,20,30,40]
calculate(score)
print(score)

#lucky number
def luckyNumber(number):
    number = 20
    return number
number=10
print(luckyNumber(number))
print(number)

#variable arguments
'''def printAll(*args):
    for arg in args:
        print(arg)
printAll(1,20,30,40)'''

#2
def multiply(*args):
    mult=1
    for number in args:
        mult=mult*number
    return mult
result = multiply(1,2,3,4)
print(result)


def multiply(start,*args):
    mult=start
    for number in args:
        mult=mult*number
    return mult
result = multiply(10,1,2,3,4)  #10 will goes to start so start value is 10, remainin willbe args values
print(result)

#**kwargs
def bottelDetails(**kwargs):
    for key,value in kwargs.items():
        print("{} : {}".format(key,value))
bottelDetails(name='zirpy',color='red',capacity=1,height=10)

###
def eatMe(apple,banana,orange):
    print(apple,banana,orange)
fruits = (10,20,30)
eatMe(*fruits)