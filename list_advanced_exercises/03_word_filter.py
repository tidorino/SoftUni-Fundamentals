text = input().split(" ")
x = [i for i in text if len(i) % 2 == 0]
print("\n".join(x))


# Друго Решение:
# def func(numb):
#     for i in numb:
#         if len(i) % 2 == 0:
#             print(i)
#
#
# text = input().split(" ")
# func(text)
