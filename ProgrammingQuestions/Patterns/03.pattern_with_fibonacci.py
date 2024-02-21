# Program 1: Fibonacci Triangle Pattern
def fibonacci_triangle_pattern(rows):
    a, b = 0, 1
    for i in range(rows):
        for j in range(i + 1):
            print(a, end=" ")
            a, b = b, a + b
        print()


# Example usage:
try:
    num_rows = int(
        input("Enter the number of rows for the Fibonacci triangle pattern: "))
    fibonacci_triangle_pattern(num_rows)
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")


# Program 2: Fibonacci Square Pattern
def fibonacci_square_pattern(rows):
    a, b = 0, 1
    for _ in range(rows):
        for _ in range(rows):
            print(a, end=" ")
            a, b = b, a + b
        print()


# Example usage:
try:
    num_rows = int(
        input("Enter the number of rows for the Fibonacci square pattern: "))
    fibonacci_square_pattern(num_rows)
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")


# Program 3: Fibonacci Right-Angled Triangle Pattern
def fibonacci_right_angle_triangle(rows):
    a, b = 0, 1
    for i in range(rows):
        for _ in range(i + 1):
            print(a, end=" ")
            a, b = b, a + b
        print()


# Example usage:
try:
    num_rows = int(input(
        "Enter the number of rows for the Fibonacci right-angled triangle pattern: "))
    fibonacci_right_angle_triangle(num_rows)
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")


# Program 4: Fibonacci Pyramid Pattern
def fibonacci_pyramid_pattern(rows):
    a, b = 0, 1
    a, b = 0, 1
    for i in range(1, rows + 1):
        row = " " * (rows-i)
        for j in range(1, i + 1):
            row = row+str(a)+" "
            a, b = b, a + b
        print(row)


# Example usage:
try:
    num_rows = int(
        input("Enter the number of rows for the Fibonacci pyramid pattern: "))
    fibonacci_pyramid_pattern(num_rows)
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")


# Program 5: Fibonacci Diamond Pattern
def fibonacci_diamond_pattern(rows):
    a, b = 0, 1
    for i in range(1, rows + 1):
        row = " " * (rows-i)
        for j in range(1, i + 1):
            row = row+str(a)+" "
            a, b = b, a + b
        print(row)

    for i in range(rows - 1, 0, -1):
        row = " " * (rows-i)
        for j in range(1, i + 1):
            row = row+str(a)+" "
            a, b = b, a + b
        print(row)


# Example usage:
try:
    num_rows = int(
        input("Enter the number of rows for the Fibonacci diamond pattern: "))
    fibonacci_diamond_pattern(num_rows)
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")
