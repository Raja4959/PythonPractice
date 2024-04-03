def dec_fun(fun):
    def concat(a,b):
        print("concatination - ",str(a)+str(b))
        return fun(a,b)
    return concat

def dec_fun2(fun):
    def mul(a,b):
        print("Multiplication - ",a*b)
        return fun(a,b)
    return mul

@dec_fun2
@dec_fun
def add(a,b):
    print(a+b)

add(1,2)
