numb_info = list(map(int, input().split(", ")))

group = 0
while numb_info:
    group += 10
    current_group = list(filter(lambda x: x <= group, numb_info))
    for item in current_group:
        numb_info.remove(item)

    print(f"Group of {group}'s: {current_group}")
