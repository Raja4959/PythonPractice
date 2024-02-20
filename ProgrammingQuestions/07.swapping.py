# 1. Swap Two Variables Using a Temporary Variable:
def swap_with_temp(a, b):
    temp = a
    a = b
    b = temp
    return a, b


# 2. Swap Two Variables Without Using a Temporary Variable:
# 3. Swap Two Variables Using Arithmetic Operations:
# def swap_with_arithmetic(a, b):
def swap_without_temp(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b


# 4. Swap Two Variables Using Tuple Unpacking:
# 5. Swap Two Variables Using Pythonic Multiple Assignment:
# def swap_pythonic(a, b):
def swap_with_tuple_unpacking(a, b):
    a, b = b, a
    return a, b


# 6. Swap Two Variables Using XOR Bitwise Operation:
def swap_with_xor(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


# 7. Swap Elements in a List:
def swap_elements_in_list(lst, index1, index2):
    lst[index1], lst[index2] = lst[index2], lst[index1]
    return lst



# 1.Example usage:
x = 5
y = 10
x, y = swap_with_temp(x, y)
print(f"After swapping: x = {x}, y = {y}")


# 2,3.Example usage:
x = 5
y = 10
x, y = swap_without_temp(x, y)
print(f"After swapping: x = {x}, y = {y}")

# 4,5.Example usage:
x = 5
y = 10
x, y = swap_with_tuple_unpacking(x, y)
print(f"After swapping: x = {x}, y = {y}")

# 6.Example usage:
x = 5
y = 10
x, y = swap_with_xor(x, y)
print(f"After swapping: x = {x}, y = {y}")

# 7.Example usage:
original_list = [1, 2, 3, 4, 5]
index_to_swap1 = 1
index_to_swap2 = 3
swapped_list = swap_elements_in_list(
    original_list, index_to_swap1, index_to_swap2)
print(
    f"After swapping elements at indices {index_to_swap1} and {index_to_swap2}: {swapped_list}")