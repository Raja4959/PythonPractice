# write python program to return index pairs whose sum is zero
# input = [-22, 1, 3, 14, -5, 4, 6, 5, 22]
# output = [(0, 8), (4, 7)]

a = [-22, 1, 3, 14, -5, 4, 6, 5, 22]
# ((0, 8), (4, 7))
res = []
tried = []
for i in a:
    try:
        n = -1 * i
        if n in tried:
            continue
        tried.append(i)
        s = a.index(i)
        e = a.index(n)
    except Exception as e:
        continue
    else:
        res.append((s, e))

print(res)
