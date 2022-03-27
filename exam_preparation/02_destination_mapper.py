import re

pattern = r'([=\/])([A-Z][A-Za-z]{2,})\1'
info = input()

result = re.finditer(pattern, info)
total_points = 0
my_list = []

for word in result:
    city = word[2]
    my_list.append(city)
    total_points += len(city)

print(f'Destinations: {", ".join(my_list)}')

print(f'Travel Points: {total_points}')
