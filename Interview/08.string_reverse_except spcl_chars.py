# Write a function to reverse words in the sentence.
# Sentence will contain a to z characters, spaces, commas and dots only.
# For example:
# Input: My, name, is. Shahrukh. Khan
# Output: yM, eman, si. hkurhahS. nahK
# Input: My,name.is Basavaraj
# Output: yM,eman.si jaravasaB

def reverse_words_except_special_chars(input_string):
    # Helper function to check if a character is alphanumeric
    def is_alphanumeric(char):
        return char.isalnum()

    # Split the input string into words and special characters
    words_and_special_chars = []
    current_word = ''
    for char in input_string:
        if is_alphanumeric(char):
            current_word += char
        else:
            if current_word:
                words_and_special_chars.append(current_word)
                current_word = ''
            words_and_special_chars.append(char)
    if current_word:
        words_and_special_chars.append(current_word)

    # Reverse the words
    reversed_words = [word[::-1]
                      for word in words_and_special_chars if is_alphanumeric(word)]

    # Concatenate the reversed words with the special characters
    result = ''
    for i, char in enumerate(words_and_special_chars):
        if is_alphanumeric(char):
            result += reversed_words.pop(0)
        else:
            result += char

    return result


# Example usage:
# input_string = "hello! world@"
# input_string = "My,name.is Basavaraj"
input_string = "My, Name, is. Shahrukh. Khan"
print("Original string:", input_string)
print("Modified string:", reverse_words_except_special_chars(input_string))


# simplified solution
def reverse_words_except_special_chars(input_string):
    def is_alphanumeric(char):
        return char.isalnum()
    current_word = ''
    res = ''
    for char in input_string:
        if is_alphanumeric(char):
            current_word += char
        else:
            if current_word:
                res = res + current_word[::-1]
                current_word = ''
            res = res + char
    if current_word:
        res = res + current_word[::-1]
    return res
