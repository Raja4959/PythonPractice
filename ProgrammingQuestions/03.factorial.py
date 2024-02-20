# the product of all positive integers less than or equal to a given non-negative integer
# The factorial function is defined as follows:
# n!=n×(n−1)×(n−2)×…×3×2×1
# By convention, 0!=1, which serves as the base case for the recursion.

# For example:
# 5!=5×4×3×2×1=120
# 4!=4×3×2×1=24
# 1!=1
# 0!=1 (by convention)

# 1. Calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


# 2. Recursive approach to calculate factorial
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


# 3. Generate a list of factorials up to a specified term
def generate_factorials(n):
    factorials = [factorial(i) for i in range(n)]
    return factorials


# 1.Example usage:
number = 5
result = factorial(number)
print(f"The factorial of {number} is: {result}")

# 2.Example usage:
number = 5
result = factorial_recursive(number)
print(f"The factorial of {number} (using recursion) is: {result}")

# 3.Example usage:
terms = 6
result = generate_factorials(terms)
print(f"The factorials of the first {terms} numbers are: {result}")
