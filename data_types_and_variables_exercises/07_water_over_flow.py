number_lines = int(input())
capacity = 0

for i in range(number_lines):
    liters_of_water = int(input())
    if capacity <= 255:
        capacity += liters_of_water

    if capacity > 255:
        print(f"Insufficient capacity!")
        capacity -= liters_of_water
        continue

print(capacity)
