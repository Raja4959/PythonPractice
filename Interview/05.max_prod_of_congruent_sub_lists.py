# To find the minimum and maximum product of congruence subarrays of an array
# Input1: [3, 2, -1, -2]
# Output1: 6
# Input2: [1, 0, 5]
# Output2: 5


def max_product_of_congruence_subarrays(nums):
    # Initialize variables to keep track of maximum product ending at the current index
    max_ending_here = min_ending_here = max_so_far = min_so_far = nums[0]

    # Iterate through the array starting from the second element
    for num in nums[1:]:
        # Update maximum product ending at the current index
        temp_max = max(num, max_ending_here * num, min_ending_here * num)
        temp_min = min(num, max_ending_here * num, min_ending_here * num)
        max_ending_here = temp_max
        min_ending_here = temp_min

        # Update maximum product seen so far
        max_so_far = max(max_so_far, max_ending_here)
        min_so_far = min(min_so_far, min_ending_here)

    return max_so_far, min_so_far


# Test cases
input1 = [3, 2, -1, -2]
input2 = [1, 0, 5]

output1 = max_product_of_congruence_subarrays(input1)
output2 = max_product_of_congruence_subarrays(input2)

print("Input:", input1, "Output:", output1)
print("Input:", input2, "Output:", output2)


def find_contiguous_subarrays(arr):
    subarrays = []
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            subarrays.append(arr[i:j+1])
    return subarrays


# Test case
arr = [3, 2, -1, -2]
subarrays = find_contiguous_subarrays(arr)
print(subarrays)


def find_contiguous_subarrays(arr):
    subarrays = []
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            subarrays.append(arr[i:j+1])
    return subarrays


def max_product_of_subarrays(arr):
    subarrays = find_contiguous_subarrays(arr)
    subarrays = [sub for sub in subarrays if len(
        sub) != len(arr)]  # Exclude the original list
    max_product = float('-inf')

    for sub in subarrays:
        product = 1
        for num in sub:
            product *= num
        max_product = max(max_product, product)

    return max_product


# Test cases
input1 = [3, 2, -1, -2]
input2 = [1, 0, 5]

print(max_product_of_subarrays(input1))  # Output: 6
print(max_product_of_subarrays(input2))  # Output: 5
