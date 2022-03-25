#Write a program that finds all variable names in each string. 
#A variable name starts with an underscore ("_") and contains only capital and non-capital letters and digits. 
#Extract only their names without the underscore. 
#Try to do this only with regular expressions



import re

text = input()
pattern = r"\b_[a-zA-Z0-9]+\b"

result = re.findall(pattern, text)

my_list = []

for match in result:
    my_list.append(match[1:])

print(",".join(my_list))
