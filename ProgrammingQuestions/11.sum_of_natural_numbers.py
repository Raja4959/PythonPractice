# sum of first n natural numbers = n*(n+1)/2

# 1. Using a For Loop:
def sum_of_natural_numbers_for_loop(n):
    sum_result = 0
    for i in range(1, n + 1):
        sum_result += i
    return sum_result


# 2. Using a While Loop:
def sum_of_natural_numbers_while_loop(n):
    sum_result = 0
    i = 1
    while i <= n:
        sum_result += i
        i += 1
    return sum_result


# 3. Using the Formula:
def sum_of_natural_numbers_formula(n):
    return n * (n + 1) // 2


# 4. Recursive Approach:
def sum_of_natural_numbers_recursive(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_natural_numbers_recursive(n - 1)


# 5. Using a For Loop:
def sum_of_natural_numbers_in_range_for_loop(start, end):
    sum_result = 0
    for i in range(start, end + 1):
        sum_result += i
    return sum_result


# 6. Using a While Loop:
def sum_of_natural_numbers_in_range_while_loop(start, end):
    sum_result = 0
    i = start
    while i <= end:
        sum_result += i
        i += 1
    return sum_result


# 7. Using the Formula:
def sum_of_natural_numbers_in_range_formula(start, end):
    return (end * (end + 1) - start * (start - 1)) // 2


# 8. Using the `sum` function:
def sum_of_natural_numbers_in_range_sum_function(start, end):
    return sum(range(start, end + 1))


# 1.Example usage:
n = 5
result = sum_of_natural_numbers_for_loop(n)
print(f"Sum of first {n} natural numbers (using for loop): {result}")

# 2.Example usage:
n = 5
result = sum_of_natural_numbers_while_loop(n)
print(f"Sum of first {n} natural numbers (using while loop): {result}")
# 3.Example usage:
n = 5
result = sum_of_natural_numbers_formula(n)
print(f"Sum of first {n} natural numbers (using formula): {result}")

# 4.Example usage:
n = 5
result = sum_of_natural_numbers_recursive(n)
print(f"Sum of first {n} natural numbers (using recursion): {result}")

# 5.Example usage:
start_range = 1
end_range = 5
result = sum_of_natural_numbers_in_range_for_loop(start_range, end_range)
print(
    f"Sum of natural numbers from {start_range} to {end_range} (using for loop): {result}")

# 6.Example usage:
start_range = 1
end_range = 5
result = sum_of_natural_numbers_in_range_while_loop(start_range, end_range)
print(
    f"Sum of natural numbers from {start_range} to {end_range} (using while loop): {result}")

# 7.Example usage:
start_range = 1
end_range = 5
result = sum_of_natural_numbers_in_range_formula(start_range, end_range)
print(
    f"Sum of natural numbers from {start_range} to {end_range} (using formula): {result}")

# 8.Example usage:
start_range = 1
end_range = 5
result = sum_of_natural_numbers_in_range_sum_function(start_range, end_range)
print(
    f"Sum of natural numbers from {start_range} to {end_range} (using sum function): {result}")
