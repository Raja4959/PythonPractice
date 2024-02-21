import math


# 1.Calculate HCF using the math library
def calculate_hcf_method1(a, b):
    hcf = math.gcd(a, b)
    return hcf


# Example usage:
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result_method1 = calculate_hcf_method1(num1, num2)
print(f"The HCF of {num1} and {num2} using method 1 is: {result_method1}")


# 2.Calculate HCF using Euclid's Algorithm
def calculate_hcf_method2(a, b):
    while b:
        a, b = b, a % b
    hcf = a
    return hcf


# Example usage:
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result_method2 = calculate_hcf_method2(num1, num2)
print(f"The HCF of {num1} and {num2} using method 2 is: {result_method2}")
