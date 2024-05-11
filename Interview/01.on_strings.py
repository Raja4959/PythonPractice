# reverse the order of words in a sentanece
# input = 'photon interactive systems'
# output = ['systems interactive photon']
import re
s = 'photon interactive systems'
words = s.split()
rev = [words[i] for i in range(-1, ((len(words)+1)*-1), -1)]
out = [" ".join(rev)]
print("reverse of the words in given string - ", out)

# Extarct date from given sentence
# s = "India got independence on 15 aug 1947"
# sol 1


def extract_date(sentence):
    # Regular expression pattern to match dates in various formats
    date_pattern = r'\b\d{1,2} (?:[Jj]an|[fF]eb|[mM]ar|Aapr|[Mm]ay|[Jj]un|[Jj]ul|[Aa]ug|[Ss]ep|[Oo]ct|[Nn]ov|[Dd]ec) \d{4}\b|\b\d{1,2}/\d{1,2}/\d{4}\b'

    # Find all matches of the date pattern in the sentence
    dates = re.findall(date_pattern, sentence)

    return dates


# Given sentence
s = "India got independence on 15 aug 1947"

# Extract date from the sentence
dates = extract_date(s)

# Print the extracted date(s)
print("Date(s) extracted from the sentence:", dates)


# sol2
def extract_dates(sentence):
    # Regular expression pattern to match dates in various formats
    date_pattern = r'\b\d{1,2}/\d{1,2}/\d{4}\b|\b\d{1,2}-\d{1,2}-\d{4}\b|\b\d{1,2} [a-zA-Z]+ \d{4}\b'

    # Find all matches of the date pattern in the sentence
    dates = re.findall(date_pattern, sentence)

    return dates


# Example usage:
sentence = "The event will take place on 12/25/2023 and 01 January 2024."
dates = extract_dates(sentence)
print("Dates extracted from the sentence:", dates)
