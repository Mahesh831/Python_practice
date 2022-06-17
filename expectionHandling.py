import sys
class Join:
    def __init__(self):
        print("constructor")
    def welcome(self):
        print("welcome")
    def __del__(self):
        print ("destructor")
    def members(self):
            try:
                members = ['ravi','raju','rushi']
                print(members[0])
            #multiple except cluse 
            except IndexError:   
                errorInfo = sys.exc_info()
                print(errorInfo[0],errorInfo[1])
            except IOError:
                print('ioerror')
            except ImportError:
                print('importeerrror')
            except:
                print('final except')
            #else clause will be called if there is no error in ecxcept clause
            else:
                print(members)
            finally:
                print('always executes after try and except clause')
            
j1 = Join()
j1.welcome()
j1.members()