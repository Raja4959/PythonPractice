#  Python program to product list items except for self
# input = [1,2,3,4]
# output = [24, 12, 8, 6]
# iteration 1 of [1,2,3,4] - product of all except for 1 ==> 2*3*4 = 24
# iteration 2 of [1,2,3,4] - product of all except for 2 ==> 1*3*4 = 12
# iteration 3 of [1,2,3,4] - product of all except for 3 ==> 1*2*4 = 8
# iteration 4 of [1,2,3,4] - product of all except for 4 ==> 1*2*3 = 6
from copy import deepcopy
from functools import reduce


def prod(lst):
    out = []
    for i in lst:
        temp = deepcopy(lst)
        temp.remove(i)
        # res = 1
        # for i in temp:
        #     res = res*i
        # out.append(res)
        out.append(reduce(lambda a, b: a*b, temp))
    return out


lst = [1, 2, 3, 4]
print(prod(lst=lst))


# sol2
def product_except_self(nums: list):
    length = len(nums)
    res = [1] * length
    left_product = 1
    for i in range(length):
        res[i] = left_product
        left_product *= nums[i]

    right_product = 1
    for i in range(length-1, -1, -1):
        res[i] *= right_product
        right_product *= nums[i]

    return res


print(product_except_self(lst))
