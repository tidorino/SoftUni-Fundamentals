factor = int(input())
count = int(input())
list1 = []
number = 0
for numb in range(1, count + 1):
    number = numb * factor
    list1.append(number)

print(list1)
