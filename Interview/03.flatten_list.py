# Flatten a given list
# input = [1, 2, 3, [4, 5, [6]]]
# output = [1, 2, 3, 4, 5, 6]


def flatten(lst):
    flat = []
    for i in lst:
        if isinstance(i, list):
            flat.extend(flatten(i))
        else:
            flat.append(i)
    return flat


lst = [1, 2, 3, [4, 5, [6]]]
out = flatten(lst)
print(out)
