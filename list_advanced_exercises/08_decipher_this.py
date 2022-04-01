import re

text = input()
decipher_text = []

pattern = r"((?P<digit>\d+)(?P<letter>[a-z]+))"
result = re.finditer(pattern, text)

for match in result:
    dijit = int(match.group('digit'))
    letter = match.group('letter')
    dijit = chr(dijit)
    new_text = dijit + letter
    decipher_text.append(new_text)

final_list = []
for item in decipher_text:
    a, b = item[1], item[-1]
    item = item[:1] + b + item[2:-1] + a

    final_list.append(item)

print(" ".join(final_list))



