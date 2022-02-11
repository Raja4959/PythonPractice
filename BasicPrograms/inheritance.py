class A(object):
    def __init__(self, a):
        self.a = a


class B(object):
    def __init__(self, b):
        self.b = b


class C(A, B):
    def __init__(self, a, b, c):
        A.__init__(self,a)
        B.__init__(self,b)
        A.y="additional member"
        self.c = c


obj_a = A("class a")
obj_b = B("class b")

print(obj_a.a)
print(obj_b.b)

obj_c = C("class c_A","class c_B","class c_C")
print(obj_c.a)
print(obj_c.b)
print(obj_c.c)
print(obj_c.y)