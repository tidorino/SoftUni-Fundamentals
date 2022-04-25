word = input().lower().split(" ")

odd_occurrences = {}
for i in word:
    if i not in odd_occurrences.keys():
        odd_occurrences[i] = 1
    else:
        odd_occurrences[i] += 1

for (key, value) in odd_occurrences.items():
    if value % 2 != 0:
        print(key, end=" ")

# Drugo reshenie:
# for i in odd_occurrences.keys():
#     if odd_occurrences[i] % 2 != 0:
#         print(f"{i}", end=' ')
