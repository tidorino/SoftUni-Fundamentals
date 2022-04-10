import re

string = input()
pattern = r"([**]{2}[A-Z][a-z]{2,}[**]{2})|([::]{2}[A-Z][a-z]{2,}[::]{2})"
result = re.findall(pattern, string)
emoji_lst = []

for match in result:
    current_match = [el for el in match if el != '']
    emoji_lst.append(current_match)
    for i in emoji_lst:
        new = sum(ord(ch) for ch in len(i))

