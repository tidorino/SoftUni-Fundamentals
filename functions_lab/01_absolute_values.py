numbers = input().split()
number_list = list()
for n in numbers:
    current_n = abs(float(n))
    number_list.append(current_n)

print(number_list)