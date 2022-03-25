import re
# Write a program that receives a single string and extracts all email addresses from it.
# Print the extracted email addresses on separate lines. Emails are in the format "{user}@{host}", where:
# •	{user} could consist only of letters and digits; the symbols ".", "-" and "_" can appear between them
# {host} is a sequence of at least two words, each couple of words must be separated by a single dot ".".
# Each word consists of only letters and can have hyphens "-" between the letters.

text = input()


pattern = r"(?<= )[a-zA-Z0-9]+((\.|_|\-)[A-Za-z0-9]+)*@[a-zA-Z]+(-[a-zA-Z]+)*(\.[a-z]+(-[a-z]+)*)+"

result = re.finditer(pattern, text)

for email in result:
    print(email.group())


