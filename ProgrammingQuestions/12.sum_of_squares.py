# sum of first n natural numbers squares = n*(n+1)*(2n+1)/6

#1. Using a For Loop:
def sum_of_squares_in_range_for_loop(start, end):
    sum_result = 0
    for i in range(start, end + 1):
        sum_result += i**2
    return sum_result


#2. Using the sum function with a Generator Expression:
def sum_of_squares_in_range_sum_function(start, end):
    return sum(i**2 for i in range(start, end + 1))


# 3. Using the Formula for the Sum of Squares:
def sum_of_squares_in_range_formula(start, end):
    return (end * (end + 1) * (2 * end + 1) - start * (start - 1) * (2 * start - 1)) // 6

# 4. Using a For Loop:


def sum_of_squares_for_loop(n):
    sum_result = 0
    for i in range(1, n + 1):
        sum_result += i**2
    return sum_result


# 5. Using the `sum` function with a Generator Expression:
def sum_of_squares_sum_function(n):
    return sum(i**2 for i in range(1, n + 1))


# 3. Using the Formula for the Sum of Squares:
def sum_of_squares_formula(n):
    return (n * (n + 1) * (2 * n + 1)) // 6


# 1.Example usage:
start_range = 1
end_range = 5
result = sum_of_squares_in_range_for_loop(start_range, end_range)
print(
    f"Sum of squares of numbers from {start_range} to {end_range} (using for loop): {result}")

# 2.Example usage:
start_range = 1
end_range = 5
result = sum_of_squares_in_range_sum_function(start_range, end_range)
print(
    f"Sum of squares of numbers from {start_range} to {end_range} (using sum function): {result}")

# 3.Example usage:
start_range = 1
end_range = 5
result = sum_of_squares_in_range_formula(start_range, end_range)
print(
    f"Sum of squares of numbers from {start_range} to {end_range} (using formula): {result}")

# 4.Example usage:
n = 5
result = sum_of_squares_for_loop(n)
print(
    f"Sum of squares of first {n} natural numbers (using for loop): {result}")

# 5.Example usage:
n = 5
result = sum_of_squares_sum_function(n)
print(
    f"Sum of squares of first {n} natural numbers (using sum function): {result}")

# 6.Example usage:
n = 5
result = sum_of_squares_formula(n)
print(f"Sum of squares of first {n} natural numbers (using formula): {result}")
