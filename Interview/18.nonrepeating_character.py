# Have the function SearchingChallenge(str) take the str parameter being passed, which will contain only alphabetic characters and spaces, 
# and return the first non-repeating character. For example: if str is "agettkgaeee" then your program should return k. 
# The string will always contain at least one character and there will always be at least one non-repeating character.
# Examples
# Input: "abcdef"
# Output: a
# Input: "hello world hi hey"
# Output: w

def non_repeating_character(strParam):
  

  count_char = {}
  for char in strParam:
    if char in count_char:
      count_char[char] += 1
    else:
      count_char[char] = 1

  for char in strParam:
    if count_char[char] == 1:
      return char

  return strParam

# input = "agettkgaeee"
input = "abcdef"
print(non_repeating_character(input))

# Nonrepeating Character

# Have the function NonrepeatingCharacter(str) take the str parameter being passed, 
# which will contain only alphabetic characters and spaces, and return the first non-repeating character. 
# For example: if str is "agettkgaeee" then your program should return k. 
# The string will always contain at least one character and there will always be at least one non-repeating character.