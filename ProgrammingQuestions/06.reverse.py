# 1. Reverse a String:
def reverse_string(input_str):
    return input_str[::-1]

# 2. Reverse a List:


def reverse_list(input_list):
    return input_list[::-1]


# 3. Reverse an Integer:
def reverse_integer(num):
    sign = -1 if num < 0 else 1
    reversed_num = int(str(abs(num))[::-1]) * sign
    return reversed_num


# 1.Example usage:
original_string = "hello"
reversed_string = reverse_string(original_string)
print(
    f"Original String: {original_string}\nReversed String: {reversed_string}")

# 2.Example usage:
original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)
print(f"Original List: {original_list}\nReversed List: {reversed_list}")

# 3.Example usage:
original_number = 12345
reversed_number = reverse_integer(original_number)
print(
    f"Original Number: {original_number}\nReversed Number: {reversed_number}")
