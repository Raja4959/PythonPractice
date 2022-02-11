"""
- List Comprehension is alternate feature to for loop
- More concise, readable, efficient and mimic functional programmig Style
- mostly used to filter list elements and apply methods to specific elemets of the list
"""

numbers = [4, 8, 6, 9, 3]

# simple list comprehension to get cubes of list elements

cubes = [i**3 for i in numbers]
print(cubes)  # --> [64, 512, 216, 729, 27]


# applying method to list items using list comprehension
def square(num):
    return num*num


squares = [square(i) for i in numbers]
print(squares)  # --> [16, 64, 36, 81, 9]

# filtering list elements
even_numbers = [i for i in numbers if i % 2 == 0]
odd_numbers = [i for i in numbers if i % 2 != 0]
print(even_numbers)  # --> [4, 8, 6]
print(odd_numbers)  # --> [9, 3]

# applying method and filters
even_squares = [square(i) for i in numbers if i % 2 == 0]
print(even_squares)  # --> [16, 64, 36]
