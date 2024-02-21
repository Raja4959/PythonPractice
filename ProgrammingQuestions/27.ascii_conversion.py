# 1.Convert a string to ASCII
def string_to_ascii(input_string):
    ascii_list = [ord(char) for char in input_string]
    return ascii_list

# Example usage:
user_input_string = input("Enter a string: ")
ascii_representation = string_to_ascii(user_input_string)
print(f"ASCII representation of '{user_input_string}': {ascii_representation}")



# 2.Convert ASCII to a string
def ascii_to_string(ascii_list):
    output_string = ''.join(chr(ascii_val) for ascii_val in ascii_list)
    return output_string

# Example usage:
user_input_ascii = input("Enter ASCII values separated by commas: ")
ascii_list = [int(val) for val in user_input_ascii.split(',')]
result_string = ascii_to_string(ascii_list)
print(f"String representation of ASCII values {ascii_list}: '{result_string}'")
