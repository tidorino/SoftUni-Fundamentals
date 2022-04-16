import math

budget = float(input())
price_for_1kg_flour = float(input())
colored_eggs = 0
price_eggs = price_for_1kg_flour * 0.75
price_milk_1l = price_for_1kg_flour * 1.25
price_milk_250ml = price_milk_1l / 4
price_one_bread = price_eggs + price_for_1kg_flour + price_milk_250ml

number_bread = abs(budget / price_one_bread)
n_b = math.floor(number_bread)
rest_sum = budget - (n_b * price_one_bread)
received_eggs = n_b * 3
first_sum = 0
for i in range(0, n_b + 1, 3):
    if i % 3 == 0 and i != 0:
        first_sum = i - 2
        colored_eggs += first_sum

rest_eggs = received_eggs - colored_eggs

print(f'You made {n_b} loaves of Easter bread! Now you have {rest_eggs} eggs and {rest_sum:.2f}BGN left.')