# numbers = input().split(" ")
# num_list = map(int, numbers)
#
# even_numbs = list(filter(lambda x: x % 2 == 0, num_list))
# print(even_numbs)

result = list(filter(lambda x: x % 2 == 0, list(map(int, input().split(" ")))))
print(result)