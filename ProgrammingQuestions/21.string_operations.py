# 1. Count the Number of Characters in a String:
from collections import Counter


def count_characters(input_string):
    return len(input_string)


# Example usage:
user_input = input("Enter a string: ")
char_count = count_characters(user_input)
print(f"The number of characters in the string is: {char_count}")


# 2. Reverse a String:
def reverse_string(input_string):
    return input_string[::-1]


# Example usage:
user_input = input("Enter a string: ")
reversed_str = reverse_string(user_input)
print(f"The reversed string is: {reversed_str}")


# 3. Check if a String is a Palindrome:
def is_palindrome(input_string):
    return input_string == input_string[::-1]


# Example usage:
user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# 4. Count the Occurrences of a Substring in a String:
def count_substring_occurrences(main_string, substring):
    return main_string.count(substring)


# Example usage:
main_str = input("Enter the main string: ")
sub_str = input("Enter the substring to count: ")
occurrences = count_substring_occurrences(main_str, sub_str)
print(
    f"The substring '{sub_str}' occurs {occurrences} times in the main string.")


# 5. Convert a String to Uppercase:
def convert_to_uppercase(input_string):
    return input_string.upper()


# Example usage:
user_input = input("Enter a string: ")
uppercase_str = convert_to_uppercase(user_input)
print(f"The string in uppercase is: {uppercase_str}")


# 6. Count the Number of Words in a String:
def count_words(input_string):
    words = input_string.split()
    return len(words)


# Example usage:
user_input = input("Enter a string: ")
word_count = count_words(user_input)
print(f"The number of words in the string is: {word_count}")


# 7. Remove Whitespaces from a String:
def remove_whitespaces(input_string):
    return ''.join(input_string.split())


# Example usage:
user_input = input("Enter a string with whitespaces: ")
no_whitespaces_str = remove_whitespaces(user_input)
print(f"The string without whitespaces is: {no_whitespaces_str}")


# 8. Replace Substring in a String:
def replace_substring(main_string, old_substring, new_substring):
    return main_string.replace(old_substring, new_substring)


# Example usage:
main_str = input("Enter the main string: ")
old_sub_str = input("Enter the substring to replace: ")
new_sub_str = input("Enter the new substring: ")
updated_str = replace_substring(main_str, old_sub_str, new_sub_str)
print(f"The updated string is: {updated_str}")


# 9. Check if a String Starts or Ends with a Substring:
def starts_or_ends_with(input_string, substring):
    return input_string.startswith(substring), input_string.endswith(substring)


# Example usage:
user_input = input("Enter a string: ")
check_substring = input("Enter the substring to check: ")
starts_with, ends_with = starts_or_ends_with(user_input, check_substring)
print(f"The string starts with '{check_substring}': {starts_with}")
print(f"The string ends with '{check_substring}': {ends_with}")


# 10. Split a String into a List of Words:
def split_into_words(input_string):
    return input_string.split()


# Example usage:
user_input = input("Enter a string: ")
words_list = split_into_words(user_input)
print(f"The list of words in the string is: {words_list}")


# 11. Count Vowels and Consonants in a String:
def count_vowels_and_consonants(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in input_string if char in vowels)
    consonant_count = len(input_string) - vowel_count
    return vowel_count, consonant_count


# Example usage:
user_input = input("Enter a string: ")
vowels, consonants = count_vowels_and_consonants(user_input)
print(f"The number of vowels: {vowels}")
print(f"The number of consonants: {consonants}")


# 12. Capitalize the First Letter of Each Word in a String:
def capitalize_first_letter(input_string):
    return ' '.join(word.capitalize() for word in input_string.split())


# Example usage:
user_input = input("Enter a string: ")
capitalized_str = capitalize_first_letter(user_input)
print(
    f"The string with first letter capitalized in each word: {capitalized_str}")


# 13. Check if a String Contains Only Digits:
def contains_only_digits(input_string):
    return input_string.isdigit()


# Example usage:
user_input = input("Enter a string: ")
if contains_only_digits(user_input):
    print("The string contains only digits.")
else:
    print("The string contains characters other than digits.")


# 14. Join Strings in a List:
def join_strings(string_list, separator=" "):
    return separator.join(string_list)


# Example usage:
words_list = ["Hello", "World", "Python"]
separator = input("Enter the separator (default is space): ") or " "
joined_string = join_strings(words_list, separator)
print(f"The joined string: {joined_string}")


# 15. Check if a String is Titlecased:
def is_titlecased(input_string):
    return input_string.istitle()


# Example usage:
user_input = input("Enter a string: ")
if is_titlecased(user_input):
    print("The string is titlecased.")
else:
    print("The string is not titlecased.")


# 16. Find the Longest Word in a String:
def find_longest_word(input_string):
    words = input_string.split()
    longest_word = max(words, key=len)
    return longest_word


# Example usage:
user_input = input("Enter a string: ")
longest_word = find_longest_word(user_input)
print(f"The longest word in the string is: {longest_word}")


# 17. Convert a String to Title Case:
def convert_to_title_case(input_string):
    return input_string.title()


# Example usage:
user_input = input("Enter a string: ")
title_case_str = convert_to_title_case(user_input)
print(f"The string in title case is: {title_case_str}")


# 18. Check if a String Contains Only Alphanumeric Characters:
def contains_only_alphanumeric(input_string):
    return input_string.isalnum()


# Example usage:
user_input = input("Enter a string: ")
if contains_only_alphanumeric(user_input):
    print("The string contains only alphanumeric characters.")
else:
    print("The string contains characters other than alphanumeric.")


# 19. Count the Occurrences of Each Character in a String:
def count_character_occurrences(input_string):
    char_count = Counter(input_string)
    return char_count


# Example usage:
user_input = input("Enter a string: ")
char_occurrences = count_character_occurrences(user_input)
print(f"Character occurrences: {char_occurrences}")


# 20. Check if a String Contains Only Whitespaces:
def contains_only_whitespaces(input_string):
    return input_string.isspace()


# Example usage:
user_input = input("Enter a string: ")
if contains_only_whitespaces(user_input):
    print("The string contains only whitespaces.")
else:
    print("The string contains characters other than whitespaces.")


# 21. Remove Duplicates from a String:
def remove_duplicates(input_string):
    unique_chars = "".join(sorted(set(input_string), key=input_string.index))
    return unique_chars


# Example usage:
user_input = input("Enter a string with duplicates: ")
no_duplicates_str = remove_duplicates(user_input)
print(f"The string without duplicates is: {no_duplicates_str}")


# 22. Convert a String to Lowercase:
def convert_to_lowercase(input_string):
    return input_string.lower()


# Example usage:
user_input = input("Enter a string: ")
lowercase_str = convert_to_lowercase(user_input)
print(f"The string in lowercase is: {lowercase_str}")


# 23. Check if a String Contains Only Letters:
def contains_only_letters(input_string):
    return input_string.isalpha()


# Example usage:
user_input = input("Enter a string: ")
if contains_only_letters(user_input):
    print("The string contains only letters.")
else:
    print("The string contains characters other than letters.")


# 24. Find the Index of a Substring in a String:
def find_substring_index(main_string, substring):
    return main_string.find(substring)


# Example usage:
main_str = input("Enter the main string: ")
sub_str = input("Enter the substring to find: ")
index = find_substring_index(main_str, sub_str)
print(f"The index of the substring is: {index}")


# 25. Count Lines in a Multi-line String:
def count_lines(input_string):
    lines = input_string.splitlines()
    return len(lines)


# Example usage:
multi_line_input = """This is line 1.
This is line 2.
And this is line 3."""
line_count = count_lines(multi_line_input)
print(f"The number of lines in the string is: {line_count}")
