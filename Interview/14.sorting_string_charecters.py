# input = "Beautiful Is Better Than Ugly"

# Write a python script to organize letters in words more reasonably(using above string) - in an alphabetical order?

# Expected Output:

# output = 'aBefiltuu Is Beertt ahnT glUy'

str = "Beautiful Is Better Than Ugly"
words = str.split()
char_words = [list(word) for word in words]
ordered_chars = [sorted(cword, key=lambda x: x.lower())
                 for cword in char_words]
ordered_cwords = ["".join(owrd) for owrd in ordered_chars]
res = " ".join(ordered_cwords)
print(res)
