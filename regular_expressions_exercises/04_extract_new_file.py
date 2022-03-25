import re

text = input()

# pattern = r"\b[A-Za-z0-9]+(\.|_|-)?[A-Za-z0-9]+@[a-z_]+[a-z]+\.[a-z]+|(\.[a-z]+)"
pattern = r"(?<= )[a-zA-Z0-9]+((\.|_|\-)[A-Za-z0-9]+)*@[a-zA-Z]+(-[a-zA-Z]+)*(\.[a-z]+(-[a-z]+)*)+"

result = re.finditer(pattern, text)

for email in result:
    print(email.group())


