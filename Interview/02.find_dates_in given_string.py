# Extarct date from given sentence
# s = "India got independence on 15 aug 1947"


import re


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
sentence = "The event will take place on 12/25/2023 and 01 January 2024. India got independence on 15 aug 1947"
dates = extract_dates(sentence)
print("Dates extracted from the sentence:", dates)


pattern = r"\b\d{1,2}/\d{1,2}/\d{4}\b|\b\d{1,2}-\b\d{1,2}-\d{4}\b|\b\d{1,2} [a-zA-Z]+ \d{4}\b"

# Summary of Differences
# - findall: Returns all non-overlapping matches as a list of strings. Finds all occurrences.
# - search: Searches for the first match and returns a match object. Finds the first occurrence.
# - match: Checks for a match only at the beginning of the string and returns a match object. Ensures the pattern matches from the start of the string.
# When to Use Each
# - Use findall to retrieve all matches in a string.
# - Use search to find the first occurrence of a pattern.
# - Use match to verify if the string starts with a specific pattern.
