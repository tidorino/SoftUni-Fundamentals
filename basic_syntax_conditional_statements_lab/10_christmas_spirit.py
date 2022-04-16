quantity = int(input())
days = int(input())
price = 0
spirit = 0
for i in range(1, days + 1):
    if i % 11 == 0:
        quantity += 2

    if i % 2 == 0:
        price += quantity * 2
        spirit += 5

    if i % 3 == 0:
        price += quantity * 8
        spirit += 13

    if i % 5 == 0:
        price += quantity * 15
        spirit += 17

    if i % 3 == 0 and i % 5 == 0:
        spirit += 30

    if i % 10 == 0:
        price += 23
        spirit -= 20
        if i == days:
            spirit -= 30

print(f"Total cost: {price}")
print(f"Total spirit: {spirit}")