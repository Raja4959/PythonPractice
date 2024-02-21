def arithmetic_and_assignment_operations(num1, num2):
    # Addition
    sum_result = num1 + num2
    print(f"Addition: {num1} + {num2} = {sum_result}")

    # Subtraction
    difference_result = num1 - num2
    print(f"Subtraction: {num1} - {num2} = {difference_result}")

    # Multiplication
    product_result = num1 * num2
    print(f"Multiplication: {num1} * {num2} = {product_result}")

    # Division (handling division by zero)
    if num2 != 0:
        division_result = num1 / num2
        print(f"Division: {num1} / {num2} = {division_result}")
    else:
        print("Cannot divide by zero.")

    # Modulus
    modulus_result = num1 % num2 if num2 != 0 else "Cannot calculate modulus by zero"
    print(f"Modulus: {num1} % {num2} = {modulus_result}")

    # Floor Division (handling division by zero)
    floor_division_result = num1 // num2 if num2 != 0 else "Cannot perform floor division by zero"
    print(f"Floor Division: {num1} // {num2} = {floor_division_result}")

    # Exponentiation
    exponent_result = num1 ** num2
    print(f"Exponentiation: {num1} ** {num2} = {exponent_result}")

    # Assignment operators
    a = num1
    b = num2

    # Addition Assignment
    a += b
    print(f"\nAddition Assignment: a += b => a = {a}")

    # Subtraction Assignment
    a -= b
    print(f"Subtraction Assignment: a -= b => a = {a}")

    # Multiplication Assignment
    a *= b
    print(f"Multiplication Assignment: a *= b => a = {a}")

    # Division Assignment (assuming b is not zero)
    a /= b if b != 0 else a
    print(f"Division Assignment: a /= b => a = {a}")

    # Modulus Assignment (assuming b is not zero)
    a %= b if b != 0 else a
    print(f"Modulus Assignment: a %= b => a = {a}")

    # Floor Division Assignment (assuming b is not zero)
    a //= b if b != 0 else a
    print(f"Floor Division Assignment: a //= b => a = {a}")

    # Exponentiation Assignment
    a **= b
    print(f"Exponentiation Assignment: a **= b => a = {a}")

# Example usage:
try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    arithmetic_and_assignment_operations(number1, number2)
except ValueError:
    print("Invalid input. Please enter valid numerical values.")
