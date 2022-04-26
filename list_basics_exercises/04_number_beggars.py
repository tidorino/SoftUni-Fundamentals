string = input()
beggars = int(input())

string_list = string.split(', ')
earns = []

for numb in range(beggars):
    earns.append(int(0))

while string_list:
    for numb in range(beggars):
        earns[numb] += int(string_list[0])
        string_list.remove(string_list[0])
        if not string_list:
            break

print(earns)
