# The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones,
# usually starting with 0 and 1. The sequence begins:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# In mathematical terms, the Fibonacci sequence F(n) is defined by the recurrence relation:
# F(n)=F(n−1)+F(n−2)
# with initial conditions:
# F(0)=0,F(1)=1


# 1. Generate the Fibonacci sequence up to a specified term:
def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


# 2. Calculate the Nth term of the Fibonacci sequence:
def fibonacci_nth_term(n):
    if n <= 0:
        return "Invalid input, N should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b


# 3. Check if a number is a Fibonacci number:
def is_fibonacci(num):
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a == num


# 1.Example usage:
terms = 10
result = generate_fibonacci(terms)
print(f"The first {terms} terms of the Fibonacci sequence are: {result}")

# 2.Example usage:
N = 7
result = fibonacci_nth_term(N)
print(f"The {N}th term of the Fibonacci sequence is: {result}")

# 3.Example usage:
number_to_check = 21
if is_fibonacci(number_to_check):
    print(f"{number_to_check} is a Fibonacci number.")
else:
    print(f"{number_to_check} is not a Fibonacci number.")

