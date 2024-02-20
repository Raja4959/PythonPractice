# 1. Check if a string is a palindrome:
def is_palindrome(string):
    clean_string = ''.join(char.lower() for char in string if char.isalnum())
    return clean_string == clean_string[::-1]


# 2. Check if a number is a palindrome:
def is_palindrome_number(num):
    num_str = str(num)
    return num_str == num_str[::-1]


def find_palindromes_in_range(start, end):
    palindromes = []
    for num in range(start, end + 1):
        if is_palindrome_number(num):
            palindromes.append(num)
    return palindromes


# 3. Check if a linked list is a palindrome:
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def is_palindrome_linked_list(head):
    values = []
    current = head
    while current:
        values.append(current.value)
        current = current.next
    return values == values[::-1]


# 1.Example usage:
word = "radar"
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")

# 2.0Example usage:
number = 1221
if is_palindrome_number(number):
    print(f"{number} is a palindrome number.")
else:
    print(f"{number} is not a palindrome number.")

# 4.Example usage:
start_range = 100
end_range = 200
palindromes_in_range = find_palindromes_in_range(start_range, end_range)

print(f"Palindromic numbers between {start_range} and {end_range}: {palindromes_in_range}")

# 4.Example usage:
# Construct a linked list: 1 -> 2 -> 2 -> 1
linked_list = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
if is_palindrome_linked_list(linked_list):
    print("The linked list is a palindrome.")
else:
    print("The linked list is not a palindrome.")
