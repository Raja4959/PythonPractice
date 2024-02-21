
import math


# Program 1: Calculate Circle Area
def calculate_circle_area(radius):
    # Calculate Circle Area
    area = math.pi * radius**2
    return area


# Example usage:
try:
    circle_radius = float(input("Enter the radius of the circle: "))
    result_area = calculate_circle_area(circle_radius)
    print(f"Circle Area with radius {circle_radius}: {result_area:.2f}")
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")


# Program 2: Calculate Circle Radius
def calculate_circle_radius(area):
    # Calculate Circle Radius
    radius = math.sqrt(area / math.pi)
    return radius


# Example usage:
try:
    circle_area = float(input("Enter the area of the circle: "))
    result_radius = calculate_circle_radius(circle_area)
    print(f"Circle Radius with area {circle_area}: {result_radius:.2f}")
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")


# Program 3: Calculate Circle Circumference
def calculate_circle_circumference(radius):
    # Calculate Circumference
    circumference = 2 * math.pi * radius
    return circumference


# Example usage:
try:
    circle_radius = float(input("Enter the radius of the circle: "))
    result_circumference = calculate_circle_circumference(circle_radius)
    print(
        f"Circumference with radius {circle_radius}: {result_circumference:.2f}")
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")


# Program 4: Calculate Circle Diameter
def calculate_circle_diameter(radius):
    # Calculate Diameter
    diameter = 2 * radius
    return diameter


# Example usage:
try:
    circle_radius = float(input("Enter the radius of the circle: "))
    result_diameter = calculate_circle_diameter(circle_radius)
    print(f"Diameter with radius {circle_radius}: {result_diameter:.2f}")
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")


# Program 5: Calculate Circle Radius from Circumference
def calculate_radius_from_circumference(circumference):
    # Calculate Circle Radius from Circumference
    radius = circumference / (2 * math.pi)
    return radius


# Example usage:
try:
    circle_circumference = float(
        input("Enter the circumference of the circle: "))
    result_radius = calculate_radius_from_circumference(circle_circumference)
    print(
        f"Circle Radius with circumference {circle_circumference}: {result_radius:.2f}")
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")


# Program 6: Calculate Circle Circumference from Diameter
def calculate_circumference_from_diameter(diameter):
    # Calculate Circle Circumference from Diameter
    circumference = math.pi * diameter
    return circumference


# Example usage:
try:
    circle_diameter = float(input("Enter the diameter of the circle: "))
    result_circumference = calculate_circumference_from_diameter(
        circle_diameter)
    print(
        f"Circumference with diameter {circle_diameter}: {result_circumference:.2f}")
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")


# Program 7: Calculate Circle Diameter from Radius
def calculate_diameter_from_radius(radius):
    # Calculate Circle Diameter from Radius
    diameter = 2 * radius
    return diameter


# Example usage:
try:
    circle_radius = float(input("Enter the radius of the circle: "))
    result_diameter = calculate_diameter_from_radius(circle_radius)
    print(f"Diameter with radius {circle_radius}: {result_diameter:.2f}")
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")


# Program 8: Check if a Point is Inside or Outside a Circle
def is_point_inside_circle(center_x, center_y, radius, point_x, point_y):
    # Check if a point is inside the circle
    distance = math.sqrt((point_x - center_x)**2 + (point_y - center_y)**2)
    return distance <= radius


# Example usage:
try:
    circle_center_x = float(
        input("Enter the x-coordinate of the circle center: "))
    circle_center_y = float(
        input("Enter the y-coordinate of the circle center: "))
    circle_radius = float(input("Enter the radius of the circle: "))

    point_x = float(input("Enter the x-coordinate of the point: "))
    point_y = float(input("Enter the y-coordinate of the point: "))

    if is_point_inside_circle(circle_center_x, circle_center_y, circle_radius, point_x, point_y):
        print(f"The point ({point_x}, {point_y}) is inside the circle.")
    else:
        print(f"The point ({point_x}, {point_y}) is outside the circle.")
except ValueError:
    print("Invalid input. Please enter valid numerical values.")
