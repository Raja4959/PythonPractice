# 1. Sum of Digits in a Number String:
number_string = input("Enter a number as a string: ")
# Using list comprehension to get digits and summing them
sum_of_digits = sum([int(digit) for digit in number_string if digit.isdigit()])
print(f"Sum of digits in the number: {sum_of_digits}")


# 2. Convert Number String to Integer:
number_string = input("Enter a number as a string: ")
try:
    integer_number = int(number_string)
    print(f"Integer representation of the number: {integer_number}")
except ValueError:
    print("Invalid input. Please enter a valid number string.")


# 3. Count the Number of Digits in a Number String:
number_string = input("Enter a number as a string: ")
count_of_digits = sum(1 for digit in number_string if digit.isdigit())
print(f"Number of digits in the number: {count_of_digits}")


# 4. Check if the Number String is Palindrome:
number_string = input("Enter a number as a string: ")
if number_string == number_string[::-1]:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")


# 5.. Check if a Number is in a String:
def is_number_in_string(input_string):
    for char in input_string:
        if char.isdigit():
            return True
    return False


# 5.Example usage:
user_input = input("Enter a string: ")
if is_number_in_string(user_input):
    print("The string contains a number.")
else:
    print("The string does not contain a number.")


# 6. Find and Print Numbers in a String:
def find_numbers_in_string(input_string):
    numbers_found = [char for char in input_string if char.isdigit()]
    return numbers_found


# 6.Example usage:
user_input = input("Enter a string: ")
numbers_found = find_numbers_in_string(user_input)
if numbers_found:
    print("Numbers found in the string:", ' '.join(numbers_found))
else:
    print("No numbers found in the string.")
