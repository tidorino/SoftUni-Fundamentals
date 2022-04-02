# Write a program that reads a string from the console and
# replaces any sequence of the same letters with a single corresponding letter

text = input()
new_text = list(text)

for index in range(len(text)-1, 0, -1):
    if text[index] == text[index-1]:
        new_text.pop(index)

print("".join(new_text))
