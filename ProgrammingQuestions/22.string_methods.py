def string_methods_demo(input_string):
    # String methods demonstration
    print(f"Original String: '{input_string}'")

    # 1. Uppercase and Lowercase
    print("Uppercase:", input_string.upper())
    print("Lowercase:", input_string.lower())

    # 2. Capitalize and Title
    print("Capitalize:", input_string.capitalize())
    print("Title Case:", input_string.title())

    # 3. Check for Alphanumeric
    print("Is Alphanumeric:", input_string.isalnum())

    # 4. Check for Alphabetical
    print("Is Alphabetical:", input_string.isalpha())

    # 5. Check for Digits
    print("Is Digit:", input_string.isdigit())

    # 6. Check for Whitespace
    print("Is Whitespace:", input_string.isspace())

    # 7. Count Occurrences
    char_count = input("Enter a character to count occurrences: ")
    print(f"Occurrences of '{char_count}': {input_string.count(char_count)}")

    # 8. Find Substring
    sub_str = input("Enter a substring to find: ")
    print(f"Index of '{sub_str}': {input_string.find(sub_str)}")

    # 9. Replace Substring
    old_sub_str = input("Enter the substring to replace: ")
    new_sub_str = input("Enter the new substring: ")
    print("After replacement:", input_string.replace(old_sub_str, new_sub_str))

    # 10. Split into Words
    print("Words in the string:", input_string.split())

    # 11. Join Strings in a List
    words_list = input_string.split()
    separator = input("Enter the separator (default is space): ") or " "
    joined_string = separator.join(words_list)
    print(f"The joined string: {joined_string}")

    # 12. Strip Whitespaces
    print("Stripped of leading and trailing whitespaces:", input_string.strip())

# Example usage:
user_input = input("Enter a string: ")
string_methods_demo(user_input)
