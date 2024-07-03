# write a python program to check if each charecter from string1 is available in string2
# each char should be present and char count in string1 should be >= the char count in string2
s1 = "asda"
s2 = "dsaaaasda"
# s1 = "asda"
# s2 = "asdd"

string1 = list(s1)
string2 = list(s2)
res = [False if not string1.count(
    i) <= string2.count(i) else True for i in string1]
print(all(res))


# to find whether have substring or not
# sol2
def is_subsequence(S1, S2):
    iter_s2 = iter(S2)
    return all(char in iter_s2 for char in S1)


# Test cases
input1_s1 = "asda"
input1_s2 = "dssdba"
print(is_subsequence(input1_s1, input1_s2))

input2_s1 = "asda"
input2_s2 = "asdd"
print(is_subsequence(input2_s1, input2_s2))
