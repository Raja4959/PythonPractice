class A(object):
    class_a = [1,2,3]
    def __init__(self, a):
        self.a = a


class B(object):
    def __init__(self, b):
        self.b = b


class C(A, B):
    def __init__(self, a, b, c):
        # A.__init__(self,a)
        super().__init__(self,b)
        # print(super().class_a )
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
print(obj_c.class_a)
print(obj_c.y)