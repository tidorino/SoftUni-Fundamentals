numb = int(input())

for i in range(1, numb + 1):
    for y in range(0, i):
        print('*', end="")
    print()
for i in range(numb - 1, - 1, - 1):
    for y in range(0, i):
        print('*', end="")
    print()
