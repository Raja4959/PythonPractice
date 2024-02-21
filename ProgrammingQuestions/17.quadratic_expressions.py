# 1. Calculate Roots of Quadratic Equation:
import cmath


def quadratic_roots(a, b, c):
    # Calculate the discriminant
    discriminant = cmath.sqrt(b**2 - 4*a*c)

    # Calculate the roots
    root1 = (-b + discriminant) / (2*a)
    root2 = (-b - discriminant) / (2*a)

    return root1, root2


# Example usage:
a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))

roots = quadratic_roots(a, b, c)
print(f"The roots of the quadratic equation are: {roots}")


# 2. Determine Nature of Roots of Quadratic Equation:
def nature_of_roots(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        return "Real and Distinct Roots"
    elif discriminant == 0:
        return "Real and Equal Roots"
    else:
        return "Complex Roots"


# Example usage:
a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))

nature = nature_of_roots(a, b, c)
print(f"The nature of roots of the quadratic equation is: {nature}")
