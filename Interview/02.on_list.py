# Flatten a given list
# input = [1, 2, 3, [4, 5, [6]]]
# output = [1, 2, 3, 4, 5, 6]
from copy import deepcopy


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

#  Python program to multiply list items except for self
# input = [1,2,3,4]
# output = [24, 12, 8, 6]
# iteration 1 of [1,2,3,4] - product of all except for 1 ==> 2*3*4 = 24
# iteration 2 of [1,2,3,4] - product of all except for 2 ==> 1*3*4 = 12
# iteration 3 of [1,2,3,4] - product of all except for 3 ==> 1*2*4 = 8
# iteration 4 of [1,2,3,4] - product of all except for 4 ==> 1*2*3 = 6


def prod(lst):
    res = 1
    for i in lst:
        res = res*i
    return res


lst = [1, 2, 3, 4]
out = []
for i in lst:
    t = deepcopy(lst)
    t.remove(i)
    print(t)
    out.append(prod(t))
print(out)

# To find the maximum product of congruence subarrays of an array
# Input1: [3, 2, -1, -2]
# Output1: 6
# Input2: [1, 0, 5]
# Output2: 5


def max_product_of_congruence_subarrays(nums):
    # Initialize variables to keep track of maximum product ending at the current index
    max_ending_here = min_ending_here = max_so_far = nums[0]

    # Iterate through the array starting from the second element
    for num in nums[1:]:
        # Update maximum product ending at the current index
        temp_max = max(num, max_ending_here * num, min_ending_here * num)
        min_ending_here = min(num, max_ending_here *
                              num, min_ending_here * num)
        max_ending_here = temp_max

        # Update maximum product seen so far
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


# Test cases
input1 = [3, 2, -1, -2]
input2 = [1, 0, 5]

output1 = max_product_of_congruence_subarrays(input1)
output2 = max_product_of_congruence_subarrays(input2)

print("Input:", input1, "Output:", output1)
print("Input:", input2, "Output:", output2)
