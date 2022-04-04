numbers = list(map(int, input().split(", ")))

positive = [str(i) for i in numbers if i >= 0]
negative = [str(i) for i in numbers if i < 0]
even = [str(i) for i in numbers if i % 2 == 0]
odd = [str(i) for i in numbers if i % 2 != 0]

print(f'Positive: {", ".join(positive)}')
print(f'Negative: {", ".join(negative)}')
print(f'Even: {", ".join(even)}')
print(f'Odd: {", ".join(odd)}')


# Друго решение:
# def func(num):
#     list1 = []
#     list2 = []
#     list3 = []
#     list4 = []
#     for i in num:
#         if i >= 0:
#             list1.append(str(i))
#         else:
#             list2.append(str(i))
#         if i % 2 == 0:
#             list3.append(str(i))
#
#         else:
#             list4.append(str(i))
#
#     print(f'Positive: {", ".join(list1)}')
#     print(f'Negative: {", ".join(list2)}')
#     print(f'Even: {", ".join(list3)}')
#     print(f'Odd: {", ".join(list4)}')
#
#
# numbers = map(int, input().split(", "))
# func(numbers)