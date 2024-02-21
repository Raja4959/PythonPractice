import random


# 1. Generate a Random Integer within a Range:
def generate_random_integer(start, end):
    return random.randint(start, end)


# 2. Generate a Random Floating-Point Number within a Range:
def generate_random_float(start, end):
    return random.uniform(start, end)


# 3. Shuffle a List of Numbers:
def shuffle_list(numbers):
    random.shuffle(numbers)
    return numbers


# 4. Randomly Select an Element from a List:
def random_element_from_list(elements):
    return random.choice(elements)


# 1.Example usage:
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))
random_number = generate_random_integer(start_range, end_range)
print(f"Random number between {start_range} and {end_range}: {random_number}")

# 2.Example usage:
start_range = float(input("Enter the start of the range: "))
end_range = float(input("Enter the end of the range: "))
random_float = generate_random_float(start_range, end_range)
print(
    f"Random floating-point number between {start_range} and {end_range}: {random_float}")

# 3.Example usage:
numbers_list = list(range(1, 11))
print(f"Original list of numbers: {numbers_list}")
shuffled_numbers = shuffle_list(numbers_list)
print(f"Shuffled list of numbers: {shuffled_numbers}")

# 4.Example usage:
fruits = ["apple", "banana", "orange", "grape", "kiwi"]
print(f"Fruits: {fruits}")
random_fruit = random_element_from_list(fruits)
print(f"Randomly selected fruit: {random_fruit}")
