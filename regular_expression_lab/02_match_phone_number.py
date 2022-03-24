import re

text = input()
result = re.finditer(r'\+359([ -])2\1\d{3}\1\d{4}\b', text)

output = []
for match in result:
    output.append(match.group())

print(", ".join(output))