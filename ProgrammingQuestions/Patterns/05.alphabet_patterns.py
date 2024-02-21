# Program 1: Print Alphabet Triangle Pattern
def print_alphabet_triangle(rows):
    current_char = ord('A')
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(chr(current_char), end=" ")
            current_char += 1
        print()


# Example usage:
try:
    num_rows = int(
        input("Enter the number of rows for the alphabet triangle pattern: "))
    print_alphabet_triangle(num_rows)
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")


# Program 2: Print Reverse Alphabet Triangle Pattern
def print_reverse_alphabet_triangle(rows):
    current_char = ord('A')
    for i in range(rows, 0, -1):
        for j in range(1, i + 1):
            print(chr(current_char), end=" ")
            current_char += 1
        print()


# Example usage:
try:
    num_rows = int(
        input("Enter the number of rows for the reverse alphabet triangle pattern: "))
    print_reverse_alphabet_triangle(num_rows)
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")


# Program 3: Print Alphabet Pyramid Pattern
def print_alphabet_pyramid(rows):
    current_char = ord('A')
    for i in range(1, rows + 1):
        line = ' ' * (rows - i)
        for j in range(1, i + 1):
            line = line + chr(current_char)+ " "
            current_char += 1
        print(line)


# Example usage:
try:
    num_rows = int(
        input("Enter the number of rows for the alphabet pyramid pattern: "))
    print_alphabet_pyramid(num_rows)
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")


# Program 4: Print Alphabet Diamond Pattern
def print_alphabet_diamond(rows):
    current_char = ord('A')

    for i in range(1, rows + 1):
        line = ' ' * (rows - i)
        for j in range(1, i + 1):
            line = line + chr(current_char)+ " "
            current_char += 1
        print(line)

    current_char = ord('A') + rows
    for i in range(rows - 1, 0, -1):
        line = ' ' * (rows - i)
        for j in range(1, i + 1):
            current_char -= 1
            line = line + chr(current_char)+ " "
        print(line)


# Example usage:
try:
    num_rows = int(
        input("Enter the number of rows for the alphabet diamond pattern: "))
    print_alphabet_diamond(num_rows)
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")


# Program 5: Print Zigzag Alphabet Pattern
def print_zigzag_alphabet(rows):
    current_char = ord('A')

    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(chr(current_char), end=" ")
            current_char += 1
        print()

    current_char = ord('A') + rows-1
    for i in range(rows - 1, 0, -1):
        for j in range(1, i + 1):
            print(chr(current_char), end=" ")
            current_char -= 1
        print()


# Example usage:
try:
    num_rows = int(
        input("Enter the number of rows for the zigzag alphabet pattern: "))
    print_zigzag_alphabet(num_rows)
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")


# Program 6: Print Alphabet Right-Angled Triangle Pattern
def print_alphabet_right_angle_triangle(rows):
    current_char = ord('A')
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(chr(current_char), end=" ")
            current_char += 1
        print()


# Example usage:
try:
    num_rows = int(input(
        "Enter the number of rows for the alphabet right-angled triangle pattern: "))
    print_alphabet_right_angle_triangle(num_rows)
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")


# Program 7: Print Alphabet Staircase Pattern
def print_alphabet_staircase(rows):
    current_char = ord('A')+rows-1
    for i in range(rows, 0, -1):
        row = '  ' * (i - 1) + chr(current_char)
        current_char -= 1
        print(row)
    print("Reverse stairs")
    current_char = ord('A')+rows-1
    for i in range(1,rows+1):
        row = '  ' * (i - 1) + chr(current_char)
        current_char -= 1
        print(row)


# Example usage:
try:
    num_rows = int(
        input("Enter the number of rows for the alphabet staircase pattern: "))
    print_alphabet_staircase(num_rows)
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")
