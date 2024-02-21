import math


# Program 1: Calculate Triangle Area
def calculate_triangle_area(base, height):
    # Calculate the area of a triangle
    area = 0.5 * base * height
    return area


# Example usage:
try:
    triangle_base = float(input("Enter the base of the triangle: "))
    triangle_height = float(input("Enter the height of the triangle: "))

    result_triangle_area = calculate_triangle_area(
        triangle_base, triangle_height)
    print(
        f"Triangle Area with base {triangle_base} and height {triangle_height}: {result_triangle_area:.2f}")
except ValueError:
    print("Invalid input. Please enter valid numerical values.")


# Program 2: Calculate Triangle Perimeter
def calculate_triangle_perimeter(side1, side2, side3):
    # Calculate the perimeter of a triangle
    perimeter = side1 + side2 + side3
    return perimeter


# Example usage:
try:
    triangle_side1 = float(
        input("Enter the length of side 1 of the triangle: "))
    triangle_side2 = float(
        input("Enter the length of side 2 of the triangle: "))
    triangle_side3 = float(
        input("Enter the length of side 3 of the triangle: "))

    result_triangle_perimeter = calculate_triangle_perimeter(
        triangle_side1, triangle_side2, triangle_side3)
    print(
        f"Triangle Perimeter with sides {triangle_side1}, {triangle_side2}, {triangle_side3}: {result_triangle_perimeter:.2f}")
except ValueError:
    print("Invalid input. Please enter valid numerical values.")


# Program 3: Check the Type of Triangle
def check_triangle_type(side1, side2, side3):
    # Check the type of triangle (Equilateral, Isosceles, Scalene)
    if side1 == side2 == side3:
        return "Equilateral Triangle"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "Isosceles Triangle"
    else:
        return "Scalene Triangle"


# Example usage:
try:
    triangle_side1 = float(
        input("Enter the length of side 1 of the triangle: "))
    triangle_side2 = float(
        input("Enter the length of side 2 of the triangle: "))
    triangle_side3 = float(
        input("Enter the length of side 3 of the triangle: "))

    result_triangle_type = check_triangle_type(
        triangle_side1, triangle_side2, triangle_side3)
    print(
        f"The triangle with sides {triangle_side1}, {triangle_side2}, {triangle_side3} is a {result_triangle_type}.")
except ValueError:
    print("Invalid input. Please enter valid numerical values.")


# Program 4: Calculate Triangle Semiperimeter and Area using Heron's Formula


def calculate_triangle_semiperimeter(side1, side2, side3):
    # Calculate the semiperimeter of a triangle
    semiperimeter = (side1 + side2 + side3) / 2
    return semiperimeter


def calculate_triangle_area_herons_formula(side1, side2, side3):
    # Calculate the area of a triangle using Heron's Formula
    s = calculate_triangle_semiperimeter(side1, side2, side3)
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return area


# Example usage:
try:
    triangle_side1 = float(
        input("Enter the length of side 1 of the triangle: "))
    triangle_side2 = float(
        input("Enter the length of side 2 of the triangle: "))
    triangle_side3 = float(
        input("Enter the length of side 3 of the triangle: "))

    result_triangle_area_herons_formula = calculate_triangle_area_herons_formula(
        triangle_side1, triangle_side2, triangle_side3)
    print(
        f"Triangle Area using Heron's Formula with sides {triangle_side1}, {triangle_side2}, {triangle_side3}: {result_triangle_area_herons_formula:.2f}")
except ValueError:
    print("Invalid input. Please enter valid numerical values.")


# Program 5: Check if a Triangle is Right-Angled
def check_right_triangle(side1, side2, side3):
    # Check if a triangle is right-angled
    sides = sorted([side1, side2, side3])
    return sides[0]**2 + sides[1]**2 == sides[2]**2


# Example usage:
try:
    triangle_side1 = float(
        input("Enter the length of side 1 of the triangle: "))
    triangle_side2 = float(
        input("Enter the length of side 2 of the triangle: "))
    triangle_side3 = float(
        input("Enter the length of side 3 of the triangle: "))

    if check_right_triangle(triangle_side1, triangle_side2, triangle_side3):
        print("The triangle is a right-angled triangle.")
    else:
        print("The triangle is not a right-angled triangle.")
except ValueError:
    print("Invalid input. Please enter valid numerical values.")
