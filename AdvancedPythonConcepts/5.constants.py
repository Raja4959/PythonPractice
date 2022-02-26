def constant(f):
    def fset(self,value):
        raise TypeError("Assigning Value To a Constant")
    def fget(self):
        return f()
    return property(fget,fset)

class Constant:
    @constant
    def PI():
        return 3.14
    @constant
    def GRAVITY():
        return 9.8
c = Constant()
print(c.PI) #--> 3.14
print(c.GRAVITY) #-->9.8

c.PI = 22/7
# Traceback (most recent call last):
#   File "5.constants.py", line 19, in <module>
#     c.PI = 22/7
#   File "5.constants.py", line 3, in fset
#     raise TypeError("Assigning Value To Constant")
# TypeError: Assigning Value To Constant

