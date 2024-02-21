import math


# 1. Check if a Number is Even or Odd:
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Example usage:
user_number = int(input("Enter a number: "))
result = check_even_odd(user_number)
print(f"The number is {result}.")


# 2.Check if a Number is Positive, Negative, or Zero:
def check_positive_negative_zero(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


# Example usage:
user_number = float(input("Enter a number: "))
result = check_positive_negative_zero(user_number)
print(f"The number is {result}.")


# 3.Check if a Number is Perfect:
# a perfect number is a positive integer that is equal to the sum of its positive divisors
def is_perfect_number(number):
    divisors_sum = sum(i for i in range(1, number) if number % i == 0)
    return number == divisors_sum


# Example usage:
user_number = int(input("Enter a number: "))
if is_perfect_number(user_number):
    print(f"{user_number} is a perfect number.")
else:
    print(f"{user_number} is not a perfect number.")


# 4.Check if a Number is a Triangular Number
# A Triangular Number is a type of figurate number, like square numbers and pentagonal numbers, formed by arranging objects in an equilateral triangle.
# In simpler terms, it's the sum of consecutive natural numbers from 1 up to a specific number n.
# Tn = n(n + 1)/2
# T1 = 1 (1 dot)
# T2 = 3 (1 + 2 dots)
# T3 = 6 (1 + 2 + 3 dots)
# T4 = 10 (1 + 2 + 3 + 4 dots)
# T5 = 15 (1 + 2 + 3 + 4 + 5 dots)
# T3 = 6 is refpresented as below
#     1
#   2   3
# 4   5   6
def is_triangular_number(number):
    n = 1
    while True:
        triangular = n * (n + 1) // 2
        if triangular == number:
            return True
        elif triangular > number:
            return False
        n += 1


# Example usage:
user_number = int(input("Enter a number: "))
if is_triangular_number(user_number):
    print(f"{user_number} is a triangular number.")
else:
    print(f"{user_number} is not a triangular number.")


# 5.Check if a Number is a Perfect Square:
def is_perfect_square(number):
    root = int(number**0.5)
    return root**2 == number


# Example usage:
user_number = int(input("Enter a number: "))
if is_perfect_square(user_number):
    print(f"{user_number} is a perfect square.")
else:
    print(f"{user_number} is not a perfect square.")


# 6.Count Digits in a Number:
def count_digits(number):
    return len(str(abs(number)))


# Example usage:
user_number = int(input("Enter a number: "))
result = count_digits(user_number)
print(f"The number of digits in {user_number} is: {result}")


# 7.Check if a Number is a Perfect Cube:
def is_perfect_cube(number):
    root = round(number**(1/3))
    return root**3 == number


# Example usage:
user_number = int(input("Enter a number: "))
if is_perfect_cube(user_number):
    print(f"{user_number} is a perfect cube.")
else:
    print(f"{user_number} is not a perfect cube.")


# 8.Sum of Digits in a Number:
def sum_of_digits(number):
    return sum(int(digit) for digit in str(abs(number)))


# Example usage:
user_number = int(input("Enter a number: "))
result = sum_of_digits(user_number)
print(f"The sum of digits in {user_number} is: {result}")


# 9.Check if a Number is a Harshad (Niven) Number:
def is_harshad_number(number):
    return number % sum_of_digits(number) == 0


# Example usage:
user_number = int(input("Enter a number: "))
if is_harshad_number(user_number):
    print(f"{user_number} is a Harshad (Niven) number.")
else:
    print(f"{user_number} is not a Harshad (Niven) number.")


# 10.Find the Square Root of a Number using Newton's Method:
def square_root_newton_method(number, tolerance=1e-10):
    estimate = number
    while abs(estimate * estimate - number) > tolerance:
        estimate = (estimate + number / estimate) / 2
    return estimate


# Example usage:
user_number = float(input("Enter a positive number: "))
if user_number > 0:
    result = square_root_newton_method(user_number)
    print(f"The square root of {user_number} is approximately: {result}")
else:
    print("Please enter a positive number.")


# 11.Check if a Number is a Happy Number:
def is_happy_number(number):
    seen = set()
    while number != 1 and number not in seen:
        seen.add(number)
        number = sum(int(digit) ** 2 for digit in str(number))
    return number == 1


# Example usage:
user_number = int(input("Enter a number: "))
if is_happy_number(user_number):
    print(f"{user_number} is a happy number.")
else:
    print(f"{user_number} is not a happy number.")


# 12.Check if a Number is a Palindromic Prime:
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def is_palindrome_number(number):
    num_str = str(number)
    return num_str == num_str[::-1]


def is_palindromic_prime(number):
    return is_prime(number) and is_palindrome_number(number)


# Example usage:
user_number = int(input("Enter a number: "))
if is_palindromic_prime(user_number):
    print(f"{user_number} is a palindromic prime number.")
else:
    print(f"{user_number} is not a palindromic prime number.")


# 13.Check if a Number is a Pronic Number:
def is_pronic_number(number):
    return any(i * (i + 1) == number for i in range(int(number**0.5) + 1))


# Example usage:
user_number = int(input("Enter a number: "))
if is_pronic_number(user_number):
    print(f"{user_number} is a pronic number.")
else:
    print(f"{user_number} is not a pronic number.")


# 14.Convert Decimal to Roman Numeral:
def decimal_to_roman(decimal_num):
    roman_numerals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    roman_numeral = ''
    for value, numeral in roman_numerals:
        while decimal_num >= value:
            roman_numeral += numeral
            decimal_num -= value
    return roman_numeral


# Example usage:
user_decimal = int(input("Enter a decimal number (1 to 3999): "))
if 1 <= user_decimal <= 3999:
    roman_representation = decimal_to_roman(user_decimal)
    print(
        f"The Roman numeral representation of {user_decimal} is: {roman_representation}")
else:
    print("Please enter a valid decimal number in the range 1 to 3999.")


# 15. Calculate Exponential of a Number:
def calculate_exponential(base, exponent):
    return base ** exponent


# Example usage:
base_num = float(input("Enter the base: "))
exponent_num = float(input("Enter the exponent: "))
result = calculate_exponential(base_num, exponent_num)
print(
    f"The exponential of {base_num} to the power of {exponent_num} is: {result}")


# 16.Check if a Number is a Mersenne Prime:
def is_mersenne_prime(number):
    return is_prime(number) and bin(number + 1).count('1') == 1


# Example usage:
user_number = int(input("Enter a number: "))
if is_mersenne_prime(user_number):
    print(f"{user_number} is a Mersenne prime number.")
else:
    print(f"{user_number} is not a Mersenne prime number.")


# 17.Find the Median of Three Numbers:
def find_median_of_three_numbers(num1, num2, num3):
    numbers = [num1, num2, num3]
    numbers.sort()
    return numbers[1]


# Example usage:
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
median = find_median_of_three_numbers(num1, num2, num3)
print(f"The median of {num1}, {num2}, and {num3} is: {median}")


# 18.Check if a Number is a Strong Number:
def is_strong_number(number):
    def factorial_digit(digit):
        return math.factorial(int(digit))

    return number == sum(factorial_digit(digit) for digit in str(number))


# Example usage:
user_number = int(input("Enter a number: "))
if is_strong_number(user_number):
    print(f"{user_number} is a strong number.")
else:
    print(f"{user_number} is not a strong number.")
