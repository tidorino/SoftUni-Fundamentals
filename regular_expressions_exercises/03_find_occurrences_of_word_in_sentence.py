import re

text = input()

current_word = input()

result = re.findall(rf"{current_word}\b", text, re.I)

print(len(result))
