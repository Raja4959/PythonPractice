# Program 1: Print a Number Triangle Pattern
def print_number_triangle(rows):
    for i in range(1, rows + 1):
        row = " " * (rows-i)
        for j in range(1, i + 1):
            row = row+str(j)+" "
        print(row)


# Example usage:
try:
    num_rows = int(
        input("Enter the number of rows for the number triangle pattern: "))
    print_number_triangle(num_rows)
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")


# Program 2: Print a Number Square Pattern
def print_number_square(rows):
    for i in range(1, rows + 1):
        for j in range(1, rows + 1):
            print(j, end=" ")
        print()


# Example usage:
try:
    num_rows = int(
        input("Enter the number of rows for the number square pattern: "))
    print_number_square(num_rows)
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")


# Program 3: Print a Number Right-Angled Triangle Pattern
def print_number_right_angle_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


# Example usage:
try:
    num_rows = int(
        input("Enter the number of rows for the number right-angled triangle pattern: "))
    print_number_right_angle_triangle(num_rows)
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")


# Program 4: Print a Number Pyramid Pattern
def print_number_pyramid(rows):
    for i in range(1, rows + 1):
        row = " " * (rows-i)
        for j in range(1, i + 1):
            row = row+str(j)+" "
        print(row)


# Example usage:
try:
    num_rows = int(
        input("Enter the number of rows for the number pyramid pattern: "))
    print_number_pyramid(num_rows)
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")


# Program 5: Print a Number Diamond Pattern
def print_number_diamond(rows):
    for i in range(1, rows + 1):
        row = " " * (rows-i)
        for j in range(1, i + 1):
            row = row+str(j)+" "
        print(row)

    for i in range(rows - 1, 0, -1):
        row = " " * (rows-i)
        for j in range(1, i + 1):
            row = row+str(j)+" "
        print(row)


# Example usage:
try:
    num_rows = int(
        input("Enter the number of rows for the number diamond pattern: "))
    print_number_diamond(num_rows)
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")


# Program 6: Print a Number Hourglass Pattern
def print_number_hourglass(rows):
    for i in range(1, rows + 1):
        row = ' ' * (i - 1)
        for j in range(1, rows - i + 2):
           row = row+str(j)+" "
        print(row)

    for i in range(rows - 1, 0, -1):
        row = ' ' * (i - 1)
        for j in range(1, rows - i + 2):
           row = row+str(j)+" "
        print(row)


# Example usage:
try:
    num_rows = int(
        input("Enter the number of rows for the number hourglass pattern: "))
    print_number_hourglass(num_rows)
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")


# Program 7: Print a Number Staircase Pattern
def print_number_staircase(rows):
    for i in range(rows, 0, -1):
        row = '  ' * (i - 1) + str(i)
        print(row)
    print("reverse stairs")
    for i in range(1,rows+1):
        row = '  ' * (i - 1) + str(i)
        print(row)


# Example usage:
try:
    num_rows = int(
        input("Enter the number of rows for the number staircase pattern: "))
    print_number_staircase(num_rows)
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")
