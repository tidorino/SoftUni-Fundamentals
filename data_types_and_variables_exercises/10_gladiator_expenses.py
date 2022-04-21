lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
shield_time_broke = 0
for i in range(1, lost_fights_count + 1):

    if i % 2 == 0:
        expenses += helmet_price
    if i % 3 == 0:
        expenses += sword_price
    if i % 2 == 0 and i % 3 == 0:
        expenses += shield_price
        shield_time_broke += 1
        if shield_time_broke % 2 == 0:
            expenses += armor_price
            shield_time_broke = 0


print(f'Gladiator expenses: {expenses:.2f} aureus')
