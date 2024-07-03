import math
a = [1, 2, 3, 4, 5, 6, 7, 8]
num = 3
# [[1, 2, 3], [4, 5, 6], [7, 8]]

i = 0
res = []
r = math.ceil(len(a)/num)

for j in range(1, r+1):
    res.append(a[i:(j*num)] if (i+num) <= len(a) else a[i:])
    i = i + num

print(res)
