
numbers = [1, 4, 7, 8, 5, 2, 0, 3, 6, 9]

even_sum = sum(filter(lambda x: not x % 2, numbers))
print(even_sum)

sum = 0
for a in numbers:
    if a % 2 == 0:
        sum = sum+a

print(sum)

