# reduce method:
# Takes two elements from a sequence and replace them with single value returned by the method given
# seq = [1,5,7,9]
# reduce(lambda a,b : a+b, seq)
# [1,5,7,9] --> [6,7,9] --> [13,9] --> 22

# filter method return a new seq with filtered elements using the method.

from functools import reduce


numbers = [1, 4, 7, 8, 5, 2, 0, 3, 6, 9]

even_sum = sum(filter(lambda x: not x % 2, numbers))
print(even_sum)


sum = 0
for a in numbers:
    if a % 2 == 0:
        sum = sum+a

print(sum)

total = reduce(lambda a, b: a+b, numbers)
print(total)
