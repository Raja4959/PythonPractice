# 1. Right-angled Triangle:
def right_angle_triangle(n):
    for i in range(1, n + 1):
        print('*' * i)


# 2. Inverted Right-angled Triangle:
def inverted_right_angle_triangle(n):
    for i in range(n, 0, -1):
        print('*' * i)


# 3. Equilateral Triangle:
# 4. Pyramid Pattern:
# def pyramid(n):
def equilateral_triangle(n):
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)


# Example usages:
right_angle_triangle(5)
print("\n")
inverted_right_angle_triangle(5)
print("\n")
equilateral_triangle(5)
print("\n")
# pyramid(5)
