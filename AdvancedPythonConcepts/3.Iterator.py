"""
Iterator:
    - iterator is an object, that allows you to traverse you though all the elements of a collection,
    regard less of its implementstion
    - values of an iterator can be accesses only one at a time in sequencial order
"""
seq = ['raja', 28, 'mca']
i = iter(seq)
print(next(i))  # -->raja
print(next(i))  # -->28
print(next(i))  # -->mca
# print(next(i))
# Traceback (most recent call last):
#   File "3.IteratorAndGenerator.py", line 12, in <module>
#     print(next(i))
# StopIteration

try:
    seq = ['raja', 28, 'mca']
    j = iter(seq)
    print(next(j))  # -->raja
    print(next(j))  # -->28
    print(next(j))  # -->mca
    print(next(j))
except StopIteration:
    print("StopIteration error")   # -->StopIteration error

