n = int(input())

for i in range(1, n + 1):
    for y in range(1, n + 1):
        for w in range(1, n + 1):

            print(f'{chr(96 + i)}{chr(96 + y)}{chr(96 + w)}')
