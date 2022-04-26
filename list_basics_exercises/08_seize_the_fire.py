type_of_fire = input().split('#')
water = int(input())
effort = 0
total_fire = 0
condition = False

print("Cells:")
for fire in type_of_fire:
    fire_info = fire.split(' = ')
    fire_type_list = fire_info[0]
    value_of_cell = int(fire_info[1])
    condition = False

    if fire_type_list == 'High':
        if 81 <= value_of_cell <= 125:
            condition = True

    elif fire_type_list == 'Medium':
        if 51 <= value_of_cell <= 80:
            condition = True

    elif fire_type_list == 'Low':
        if 1 <= value_of_cell <= 50:
            condition = True

    if condition:
        if water >= value_of_cell:
            water -= value_of_cell
            effort += value_of_cell * 0.25
            total_fire += value_of_cell
            print(f'- {value_of_cell}')

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')


