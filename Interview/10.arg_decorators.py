# Simple Decorator
def simple_deco(func):
    def swap(a, b):
        if a < b:
            a = a+b
            b = a-b
            a = a-b
        return func(a, b)
    return swap


@simple_deco
def div(a, b):
    return a/b


a = 10
b = 5
print(div(a, b))


# decorator with args - 1
def arg_deco(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res.upper()
    return wrapper


def arg_deco2(n_times: int):
    def actual_dec(func):
        def wrapper(*args, **kwargs):
            for _ in range(n_times):
                func(*args, **kwargs)
            return
        return wrapper
    return actual_dec


@arg_deco
def greet(name: str):
    return f"Hello..! {name}..!"


print(greet("Raja"))


@arg_deco2(n_times=3)
def wishes_for(name):
    print(f"Hello...{name}..!")


wishes_for("Raja")
