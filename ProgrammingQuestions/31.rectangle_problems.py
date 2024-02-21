import math


# Program 1: Calculate Rectangle Area
def calculate_rectangle_area(length, width):
    # Calculate the area of a rectangle
    area = length * width
    return area


# Example usage:
try:
    rectangle_length = float(input("Enter the length of the rectangle: "))
    rectangle_width = float(input("Enter the width of the rectangle: "))

    result_rectangle_area = calculate_rectangle_area(
        rectangle_length, rectangle_width)
    print(
        f"Rectangle Area with length {rectangle_length} and width {rectangle_width}: {result_rectangle_area:.2f}")
except ValueError:
    print("Invalid input. Please enter valid numerical values.")


# Program 2: Calculate Rectangle Perimeter
def calculate_rectangle_perimeter(length, width):
    # Calculate the perimeter of a rectangle
    perimeter = 2 * (length + width)
    return perimeter


# Example usage:
try:
    rectangle_length = float(input("Enter the length of the rectangle: "))
    rectangle_width = float(input("Enter the width of the rectangle: "))

    result_rectangle_perimeter = calculate_rectangle_perimeter(
        rectangle_length, rectangle_width)
    print(
        f"Rectangle Perimeter with length {rectangle_length} and width {rectangle_width}: {result_rectangle_perimeter:.2f}")
except ValueError:
    print("Invalid input. Please enter valid numerical values.")


# Program 3: Check if a Point is Inside or Outside a Rectangle
def is_point_inside_rectangle(rectangle_x, rectangle_y, rectangle_length, rectangle_width, point_x, point_y):
    # Check if a point is inside the rectangle
    return (
        rectangle_x <= point_x <= rectangle_x + rectangle_length and
        rectangle_y <= point_y <= rectangle_y + rectangle_width
    )


# Example usage:
try:
    rectangle_x = float(input("Enter the x-coordinate of the rectangle: "))
    rectangle_y = float(input("Enter the y-coordinate of the rectangle: "))
    rectangle_length = float(input("Enter the length of the rectangle: "))
    rectangle_width = float(input("Enter the width of the rectangle: "))

    point_x = float(input("Enter the x-coordinate of the point: "))
    point_y = float(input("Enter the y-coordinate of the point: "))

    if is_point_inside_rectangle(rectangle_x, rectangle_y, rectangle_length, rectangle_width, point_x, point_y):
        print(f"The point ({point_x}, {point_y}) is inside the rectangle.")
    else:
        print(f"The point ({point_x}, {point_y}) is outside the rectangle.")
except ValueError:
    print("Invalid input. Please enter valid numerical values.")


# Program 4: Calculate Rectangle Diagonal
def calculate_rectangle_diagonal(length, width):
    # Calculate the diagonal of a rectangle
    diagonal = math.sqrt(length**2 + width**2)
    return diagonal


# Example usage:
try:
    rectangle_length = float(input("Enter the length of the rectangle: "))
    rectangle_width = float(input("Enter the width of the rectangle: "))

    result_rectangle_diagonal = calculate_rectangle_diagonal(
        rectangle_length, rectangle_width)
    print(
        f"Rectangle Diagonal with length {rectangle_length} and width {rectangle_width}: {result_rectangle_diagonal:.2f}")
except ValueError:
    print("Invalid input. Please enter valid numerical values.")


# Program 5: Check if Two Rectangles Overlap
def do_rectangles_overlap(rect1_x, rect1_y, rect1_length, rect1_width, rect2_x, rect2_y, rect2_length, rect2_width):
    # Check if two rectangles overlap
    return (
        rect1_x < rect2_x + rect2_length and
        rect1_x + rect1_length > rect2_x and
        rect1_y < rect2_y + rect2_width and
        rect1_y + rect1_width > rect2_y
    )


# Example usage:
try:
    rect1_x = float(input("Enter the x-coordinate of the first rectangle: "))
    rect1_y = float(input("Enter the y-coordinate of the first rectangle: "))
    rect1_length = float(input("Enter the length of the first rectangle: "))
    rect1_width = float(input("Enter the width of the first rectangle: "))

    rect2_x = float(input("Enter the x-coordinate of the second rectangle: "))
    rect2_y = float(input("Enter the y-coordinate of the second rectangle: "))
    rect2_length = float(input("Enter the length of the second rectangle: "))
    rect2_width = float(input("Enter the width of the second rectangle: "))

    if do_rectangles_overlap(rect1_x, rect1_y, rect1_length, rect1_width, rect2_x, rect2_y, rect2_length, rect2_width):
        print("The rectangles overlap.")
    else:
        print("The rectangles do not overlap.")
except ValueError:
    print("Invalid input. Please enter valid numerical values.")
