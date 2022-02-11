"""
Generator:
    - Generator is an iterator object whose values are created at the time of accessing them.
    - A generator can be created using generator expression or generator method
"""
# generator expression
seq = [2, 6, 8]
x = (i**3 for i in seq)  # generator expression

print(x)  # --> <generator object <genexpr> at 0x000001C7FEB53BF8>
print(next(x))  # --> 8
print(next(x))  # --> 216
print(next(x))  # --> 512
# print(next(x))
# Traceback (most recent call last):
#   File "4.Generator.py", line 14, in <module>
#     print(next(x)) # -->
# StopIteration

""" we can handle the StopIteration error in the same way we handled in Itereator topic """

# generator method


def simple_generator():
    yield "first element"
    yield "second element"
    yield "Third element"

print(simple_generator()) # --> <generator object simple_generator at 0x000002819DCF3DB0>
y = simple_generator()
print(y) # --> <generator object simple_generator at 0x000002819DCF3DB0>
for i in y:
    print(i)
            # first element
            # second element
            # Third element

