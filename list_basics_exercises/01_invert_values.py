string = input().split(" ")
list_string = []

for numb in string:
    if int(numb) >= 0:
        list_string.append(-int(numb))
    elif int(numb) < 0:
        list_string.append(abs(int(numb)))
print(list_string)
