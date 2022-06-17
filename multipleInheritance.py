'''class class1():
    def joined(self):
        print("joined")
class class2():
    def subscribe(self):
        print("subscribed")
class class3(class1,class2):
    def comment(self):
        print("commented")
cl3 = class3()
cl3.joined()
cl3.subscribe()
cl3.comment()

#multilevel inheritance
class class1():
    def joined(self):
        print("joined")
class class2(class1):
    def subscribe(self):
        print("subscribed")
class class3(class2):
    def comment(self):
        print("commented")
cl3 = class3()
cl3.joined()
cl3.subscribe()
cl3.comment()
cl2 = class2()
cl2.joined()'''

#hierarchical inheritance
class class1():
    def joined(self):
        print("joined")
class class2(class1):
    def subscribe(self):
        print("subscribed")
class class3(class1):
    def comment(self):
        print("commented")
class class4(class1):
    def share(self):
        print("shared")
cl3 = class3()
cl3.joined()

cl2 = class2()
cl2.joined()

cl4 = class4()
cl4.joined()
