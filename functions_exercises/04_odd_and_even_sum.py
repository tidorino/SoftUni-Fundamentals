def even_odd_sums(number):
    odd_sum = 0
    even_sum = 0
    for i in number:
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
    print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')


num = map(int, list(input()))
even_odd_sums(num)

# num = int(input())
# num_str = str(num).split(" ")
#
# odd = []
# even = []
#
# for i in num_str:
#     i.split(" ")
#     for y in i:
#         if int(y) % 2 == 0:
#             even.append(int(y))
#         else:
#             odd.append(int(y))
#
# print(f'Odd sum = {sum(odd)}, Even sum = {sum(even)}')