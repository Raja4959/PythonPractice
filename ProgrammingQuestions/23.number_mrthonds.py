def numbers_operations_demo(number):
    # Number operations demonstration
    print(f"Original Number: {number}")

    # 1. Absolute Value
    print("Absolute Value:", abs(number))

    # 2. Power
    exponent = int(input("Enter an exponent for power operation: "))
    print(f"{number} raised to the power of {exponent}: {pow(number, exponent)}")

    # 3. Square Root
    import math
    print(f"Square Root of {number}: {math.sqrt(number)}")

    # 4. Ceiling and Floor
    print(f"Ceiling of {number}: {math.ceil(number)}")
    print(f"Floor of {number}: {math.floor(number)}")

    # 5. Trigonometric Functions (using radians)
    angle_rad = float(input("Enter an angle in radians for trigonometric functions: "))
    print(f"Sine of {angle_rad} radians: {math.sin(angle_rad)}")
    print(f"Cosine of {angle_rad} radians: {math.cos(angle_rad)}")
    print(f"Tangent of {angle_rad} radians: {math.tan(angle_rad)}")

    # 6. Round
    decimals = int(input("Enter the number of decimals for rounding: "))
    print(f"Rounded to {decimals} decimals: {round(number, decimals)}")

# Example usage:
user_number = float(input("Enter a number: "))
numbers_operations_demo(user_number)
