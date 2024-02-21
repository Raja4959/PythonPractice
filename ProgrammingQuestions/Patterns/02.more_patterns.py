def print_square_pattern(rows):
    for i in range(1, rows + 1):
        print('* ' * rows)


# Example usage:
try:
    num_rows = int(input("Enter the number of rows for the square pattern: "))
    print_square_pattern(num_rows)
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")


# diamond pattern
def print_diamond_pattern(rows):
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

    for i in range(rows - 1, 0, -1):
        spaces = ' ' * (rows - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)


# Example usage:
try:
    num_rows = int(input("Enter the number of rows for the diamond pattern: "))
    print_diamond_pattern(num_rows)
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")

# pyramid pattern
def print_pyramid_pattern(rows):
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)


# Example usage:
try:
    num_rows = int(input("Enter the number of rows for the pyramid pattern: "))
    print_pyramid_pattern(num_rows)
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")


# Print a Number Pyramid Pattern
def print_number_pyramid(rows):
    for i in range(1, rows + 1):
        row = " " * (rows-i)
        for j in range(1, i + 1):
            row = row+"* "
        print(row)


# Example usage:
try:
    num_rows = int(
        input("Enter the number of rows for the number pyramid pattern: "))
    print_number_pyramid(num_rows)
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")


# Print a Number Diamond Pattern
def print_number_diamond(rows):
    for i in range(1, rows + 1):
        row = " " * (rows-i)
        for j in range(1, i + 1):
            row = row+"* "
        print(row)

    for i in range(rows - 1, 0, -1):
        row = " " * (rows-i)
        for j in range(1, i + 1):
            row = row+"* "
        print(row)


# Example usage:
try:
    num_rows = int(
        input("Enter the number of rows for the number diamond pattern: "))
    print_number_diamond(num_rows)
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")


# Print a Number Hourglass Pattern
def print_number_hourglass(rows):
    for i in range(1, rows + 1):
        row = ' ' * (i - 1)
        for j in range(1, rows - i + 2):
           row = row+"* "
        print(row)

    for i in range(rows - 1, 0, -1):
        row = ' ' * (i - 1)
        for j in range(1, rows - i + 2):
           row = row+"* "
        print(row)


# Example usage:
try:
    num_rows = int(
        input("Enter the number of rows for the number hourglass pattern: "))
    print_number_hourglass(num_rows)
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")


# Print a Number Staircase Pattern
def print_number_staircase(rows):
    for i in range(rows, 0, -1):
        row = '  ' * (i - 1) + '*'
        print(row)
    print("reverse stairs")
    for i in range(1,rows+1):
        row = '  ' * (i - 1) + '*'
        print(row)


# Example usage:
try:
    num_rows = int(
        input("Enter the number of rows for the number staircase pattern: "))
    print_number_staircase(num_rows)
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")