# an n-digit number is considered an Armstrong number if the sum of its digits, each raised to the nth power, is equal to the number itself.

# To determine if 5421 is an Armstrong number, we need to calculate the sum of each digit raised to the power of the number of digits 
# (which is 4 in this case since 5421 has four digits).
# Let's perform the calculation:
# 5**4+4**4+2**4+1**4=625+256+16+1=898
# Since the sum is not equal to 5421, we can conclude that 5421 is not an Armstrong number.

# For example, let's take the number 153:
# The number of digits is 3.
# 1**3+5**3+3**3=1+125+27=153
# Since the sum is 153, we can conclude that 153 is an Armstrong number.


# 1. Check if a number is an Armstrong number:
def is_armstrong_number(num):
    order = len(str(num))
    sum_of_digits = sum(int(digit) ** order for digit in str(num))
    return num == sum_of_digits


# 2. Generate Armstrong numbers in a given range:
def generate_armstrong_numbers(start, end):
    armstrong_numbers = [num for num in range(
        start, end + 1) if is_armstrong_number(num)]
    return armstrong_numbers


# 3. Generate the first N Armstrong numbers:
def generate_n_armstrong_numbers(n):
    armstrong_numbers = []
    num = 1
    while len(armstrong_numbers) < n:
        if is_armstrong_number(num):
            armstrong_numbers.append(num)
        num += 1
    return armstrong_numbers


# Example usage:
number = 153
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

# 2.Example usage:
start_range = 100
end_range = 1000
result = generate_armstrong_numbers(start_range, end_range)
print(f"Armstrong numbers between {start_range} and {end_range}: {result}")

# 3.Example usage:
N = 15
result = generate_n_armstrong_numbers(N)
print(f"The first {N} Armstrong numbers are: {result}")
