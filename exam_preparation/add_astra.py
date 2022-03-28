import math
import re

info = input()

pattern = r"([|\|#])(?P<item>[A-Za-z ]+)\1(?P<data>[0-3][0-9]\/[0-1][0-9]\/[0-2][0-9])\1(?P<calories>[0-9]+)\1"

result = re.finditer(pattern, info)

all_calories = 0
info_food = []

for data_info in result:
    item = data_info['item']
    calories = int(data_info['calories'])
    data = data_info['data']

    all_calories += calories
    info_food.append([item, data, calories])

days_food = math.floor(all_calories / 2000)
print(f"You have food to last you for: {days_food} days!")

for key in info_food:
    print(f"Item: {key[0]}, Best before: {key[1]}, Nutrition: {key[2]}")





