import re

text = input()
pattern = r"\b_[a-zA-Z0-9]+\b"

result = re.findall(pattern, text)

my_list = []

for match in result:
    my_list.append(match[1:])

print(",".join(my_list))
