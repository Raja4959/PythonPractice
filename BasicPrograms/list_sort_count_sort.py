# [7,8,9,9,2,5,5,3,2,1]
# Result -> [1,3,7,8,2,2,5,5,9,9]
# [7,8,9,9,2,5,5,3,5,2,1]
# Result -> [1,3,7,8,2,2,9,9, 5,5,5]

a = [7,8,9,9,2,5,5,3,5,2,1]
s = set(a)
d = {}
for i in s:
    d[a.count(i)] = []
for i in s:
    d[a.count(i)].append(i)
res = []
counts = d.keys()
counts = sorted(counts)
for k,v in d.items():
    d[k]=sorted(v)
for c in counts:
    l = d[c]
    for ele in l:
        res.extend([ele]*c)

print(res)