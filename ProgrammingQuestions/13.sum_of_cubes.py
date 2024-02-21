# sum of first n natural numbers = (n * (n + 1) / 2)**2 (whole square)
import math


# 1. Using a For Loop:
def sum_of_cubes_for_loop(n):
    sum_result = 0
    for i in range(1, n + 1):
        sum_result += i**3
    return sum_result


# 2. Using the `sum` function with a Generator Expression:
def sum_of_cubes_sum_function(n):
    return sum(i**3 for i in range(1, n + 1))


# 3. Using the Formula for the Sum of Cubes:
def sum_of_cubes_formula(n):
    return (n * (n + 1) // 2)**2


# 4. Using the Math Library:
def sum_of_cubes_math_library(n):
    return math.pow(sum(range(1, n + 1)), 2)


# 5. Using a For Loop within a Range:
def sum_of_cubes_in_range_for_loop(start, end):
    sum_result = 0
    for i in range(start, end + 1):
        sum_result += i**3
    return sum_result

# 6. Using the `sum` function with a Generator Expression within a Range:


def sum_of_cubes_in_range_sum_function(start, end):
    return sum(i**3 for i in range(start, end + 1))


# 7. Using the Formula for the Sum of Cubes within a Range:
def sum_of_cubes_in_range_formula(start, end):
    return ((end * (end + 1)) // 2)**2 - (((start - 1) * start) // 2)**2


# 8. Using the Math Library within a Range:
def sum_of_cubes_in_range_math_library(start, end):
    return math.pow(sum(range(start, end + 1)), 2)


# 1.Example usage:
n = 5
result = sum_of_cubes_for_loop(n)
print(f"Sum of cubes of first {n} natural numbers (using for loop): {result}")

# 2.Example usage:
n = 5
result = sum_of_cubes_sum_function(n)
print(
    f"Sum of cubes of first {n} natural numbers (using sum function): {result}")

# 3.Example usage:
n = 5
result = sum_of_cubes_formula(n)
print(f"Sum of cubes of first {n} natural numbers (using formula): {result}")

# 4.Example usage:
n = 5
result = sum_of_cubes_math_library(n)
print(
    f"Sum of cubes of first {n} natural numbers (using math library): {result}")

# 5.Example usage:
start_range = 1
end_range = 5
result = sum_of_cubes_in_range_for_loop(start_range, end_range)
print(
    f"Sum of cubes of numbers from {start_range} to {end_range} (using for loop): {result}")

# 6.Example usage:
start_range = 1
end_range = 5
result = sum_of_cubes_in_range_sum_function(start_range, end_range)
print(
    f"Sum of cubes of numbers from {start_range} to {end_range} (using sum function): {result}")

# 7.Example usage:
start_range = 1
end_range = 5
result = sum_of_cubes_in_range_formula(start_range, end_range)
print(
    f"Sum of cubes of numbers from {start_range} to {end_range} (using formula): {result}")

# 8.Example usage:
start_range = 1
end_range = 5
result = sum_of_cubes_in_range_math_library(start_range, end_range)
print(
    f"Sum of cubes of numbers from {start_range} to {end_range} (using math library): {result}")
