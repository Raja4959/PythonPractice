
import math


# Program 1: Calculate Square Area
def calculate_square_area(side):
    # Calculate the area of a square
    area = side ** 2
    return area


# Example usage:
try:
    square_side = float(input("Enter the side length of the square: "))

    result_square_area = calculate_square_area(square_side)
    print(f"Square Area with side {square_side}: {result_square_area:.2f}")
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")


# Program 2: Calculate Square Perimeter
def calculate_square_perimeter(side):
    # Calculate the perimeter of a square
    perimeter = 4 * side
    return perimeter


# Example usage:
try:
    square_side = float(input("Enter the side length of the square: "))

    result_square_perimeter = calculate_square_perimeter(square_side)
    print(
        f"Square Perimeter with side {square_side}: {result_square_perimeter:.2f}")
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")


# Program 3: Check if a Point is Inside or Outside a Square
def is_point_inside_square(square_x, square_y, side, point_x, point_y):
    # Check if a point is inside the square
    return (
        square_x <= point_x <= square_x + side and
        square_y <= point_y <= square_y + side
    )


# Example usage:
try:
    square_x = float(input("Enter the x-coordinate of the square: "))
    square_y = float(input("Enter the y-coordinate of the square: "))
    square_side = float(input("Enter the side length of the square: "))

    point_x = float(input("Enter the x-coordinate of the point: "))
    point_y = float(input("Enter the y-coordinate of the point: "))

    if is_point_inside_square(square_x, square_y, square_side, point_x, point_y):
        print(f"The point ({point_x}, {point_y}) is inside the square.")
    else:
        print(f"The point ({point_x}, {point_y}) is outside the square.")
except ValueError:
    print("Invalid input. Please enter valid numerical values.")


# Program 4: Calculate Square Diagonal
def calculate_square_diagonal(side):
    # Calculate the diagonal of a square
    diagonal = side * math.sqrt(2)
    return diagonal


# Example usage:
try:
    square_side = float(input("Enter the side length of the square: "))

    result_square_diagonal = calculate_square_diagonal(square_side)
    print(
        f"Square Diagonal with side {square_side}: {result_square_diagonal:.2f}")
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")


# Program 5: Check if Two Squares Overlap
def do_squares_overlap(square1_x, square1_y, side1, square2_x, square2_y, side2):
    # Check if two squares overlap
    return (
        square1_x < square2_x + side2 and
        square1_x + side1 > square2_x and
        square1_y < square2_y + side2 and
        square1_y + side1 > square2_y
    )


# Example usage:
try:
    square1_x = float(input("Enter the x-coordinate of the first square: "))
    square1_y = float(input("Enter the y-coordinate of the first square: "))
    side1 = float(input("Enter the side length of the first square: "))

    square2_x = float(input("Enter the x-coordinate of the second square: "))
    square2_y = float(input("Enter the y-coordinate of the second square: "))
    side2 = float(input("Enter the side length of the second square: "))

    if do_squares_overlap(square1_x, square1_y, side1, square2_x, square2_y, side2):
        print("The squares overlap.")
    else:
        print("The squares do not overlap.")
except ValueError:
    print("Invalid input. Please enter valid numerical values.")
