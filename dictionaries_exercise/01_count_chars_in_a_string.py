# Друго решение на първа част:
# from collections import Counter
#
# word = input()
# result = Counter(word)

word = input()
count = {}

for char in word:
    if char not in count:
        count[char] = 1
    else:
        count[char] += 1

# Втора част:
for (key, value) in count.items():
    if key != " ":

        print(f"{key} -> {value}")
