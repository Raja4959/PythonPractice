# 1. Decimal to Binary, Octal, and Hexadecimal:
decimal_number = int(input("Enter a decimal number: "))

binary_representation = bin(decimal_number)
octal_representation = oct(decimal_number)
hexadecimal_representation = hex(decimal_number)

print(f"Binary: {binary_representation}")
print(f"Octal: {octal_representation}")
print(f"Hexadecimal: {hexadecimal_representation}")

# 2. Binary to Decimal, Octal, and Hexadecimal:
binary_number = input("Enter a binary number: ")

decimal_representation = int(binary_number, 2)
octal_representation = oct(decimal_representation)
hexadecimal_representation = hex(decimal_representation)

print(f"Decimal: {decimal_representation}")
print(f"Octal: {octal_representation}")
print(f"Hexadecimal: {hexadecimal_representation}")

# 3. Octal to Decimal, Binary, and Hexadecimal:
octal_number = input("Enter an octal number: ")

decimal_representation = int(octal_number, 8)
binary_representation = bin(decimal_representation)
hexadecimal_representation = hex(decimal_representation)

print(f"Decimal: {decimal_representation}")
print(f"Binary: {binary_representation}")
print(f"Hexadecimal: {hexadecimal_representation}")

# 4. Hexadecimal to Decimal, Binary, and Octal:
hexadecimal_number = input("Enter a hexadecimal number: ")

decimal_representation = int(hexadecimal_number, 16)
binary_representation = bin(decimal_representation)
octal_representation = oct(decimal_representation)

print(f"Decimal: {decimal_representation}")
print(f"Binary: {binary_representation}")
print(f"Octal: {octal_representation}")
