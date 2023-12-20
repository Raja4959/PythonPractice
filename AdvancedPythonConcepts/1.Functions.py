"""
methods in pyhton are declred using def keyword
we have class methods and static methods
we also have anonymous method or lambda expression
"""
# simple method


def simple_print():
    a = "this is simple print method"
    return a


print(simple_print())

def method_param(a):
    print(a , "is a parameter")

method_param("Weed")


div = lambda a,b: a//b
print(div(10,5))