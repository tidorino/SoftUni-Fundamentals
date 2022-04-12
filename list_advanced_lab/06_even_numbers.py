numbs = list(map(int, input().split(", ")))
new_list = []
for i in numbs:
    x = numbs.index(i)
    if i % 2 == 0:
        new_list.append(x)

print(new_list)

# По правилното решение:
# numbs = input().split(", ")
# numbs = list(map(int, numbs))
#
# new_list = []
# for i in range(len(numbs)):
#
#     if numbs[i] % 2 == 0:
#         new_list.append(i)
#
# print(new_list)