group_size = int(input())
days = int(input())

earned_coins = 0
coins_per_companion = 0
group_size = group_size
for i in range(1, days + 1):
    if i == 10 or i % 10 == 0:
        group_size -= 2

    if i == 15 or i % 15 == 0:
        group_size += 5

    earned_coins += 50
    coins_per_companion += group_size * 2

    if i % 3 == 0:
        coins_per_companion += group_size * 3
    if i % 5 == 0:
        earned_coins += group_size * 20
        if i % 5 == 0 and i % 3 == 0:
            coins_per_companion += group_size * 2


sum_for_each = earned_coins / group_size
sum_paid_coins = coins_per_companion / group_size
total_for_one = int(sum_for_each - sum_paid_coins)

print(f"{group_size} companions received {total_for_one} coins each.")
