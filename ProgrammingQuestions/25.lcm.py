import math


# 1.Calculate LCM using the formula LCM(a, b) = (a * b) / GCD(a, b)
# Calculate LCM using the property LCM(a, b) * GCD(a, b) = a * b
def calculate_lcm_using_math(a, b):
    gcd = math.gcd(a, b)
    lcm = (a * b) // gcd
    return lcm


# Example usage:
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result_method1 = calculate_lcm_using_math(num1, num2)
print(f"The LCM of {num1} and {num2} is: {result_method1}")


# 2. Calculate LCM using a while loop
def calculate_lcm_using_while(a, b):
    lcm = max(a, b)
    while True:
        if lcm % a == 0 and lcm % b == 0:
            break
        lcm += 1
    return lcm

# Example usage:
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result_method3 = calculate_lcm_using_while(num1, num2)
print(f"The LCM of {num1} and {num2} is: {result_method3}")

