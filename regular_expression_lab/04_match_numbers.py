import re

text = input()
pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
matches = re.finditer(pattern, text)
numbers = []
for match in matches:
    numbers.append(match.group())

print(" ".join(numbers))