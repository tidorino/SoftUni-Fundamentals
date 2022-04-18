import sys

f_n = int(input())
s_n = int(input())
t_n = int(input())

if f_n > s_n and f_n > t_n:
    print(f_n)
elif s_n > f_n and s_n > t_n:
    print(s_n)
else:
    print(t_n)


# max_number = - sys.maxsize
# i = 0
# y = 0
#
# for i in range(f_n, s_n + 1):
#     if i > max_number:
#         max_number = i
# for y in range(s_n, t_n + 1):
#     if y > max_number:
#         max_number = y
#
# if i > y:
#     print(i)
# else:
#     print(y)