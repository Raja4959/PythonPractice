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
