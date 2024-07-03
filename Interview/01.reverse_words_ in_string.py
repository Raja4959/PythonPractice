# Problem: reverse the order of words in a sentanece
# input = 'photon interactive systems'
# output = ['systems interactive photon']

s = 'photon interactive systems'
words = s.split()
rev = [words[i] for i in range(len(words)-1, -1, -1)]
out = [" ".join(rev)]
print("reverse of the words in given string - ", out)
