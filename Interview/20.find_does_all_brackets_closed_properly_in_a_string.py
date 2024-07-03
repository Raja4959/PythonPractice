# write a python program to find out given string is valid or not - conditions applied
# - all brackets (){}[]<> which are opened should be closed properly
# the order should be correct -- the forst opened bracket


# TODO:: to be completed
def is_valid_str(str):
    pair = ['()', '<>', '{}', '[]']
    res = True
    ord_o = []
    ord_c = []
    for i in pair:
        o = s.find(i[0])
        c = s.find(i[1])
        if o < c:
            return False
        if o >= 0:
            ord_o.append(o)
            if c >= 0:
                ord_c.append(c)
            else:
                return False
        if c >= 0 and o < 0:
            return False

    for i in range(len(pair)):

        pass

    return True


s = "(djsoo{<[dssjn]})"

res = "String is valid" if is_valid_str(s) else "String is invalid"
print(res)
