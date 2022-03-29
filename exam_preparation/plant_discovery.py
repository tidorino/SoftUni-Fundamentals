def rate_func(new_command, info_dict):
    command = new_command[1].split(" - ")
    plant = command[0]
    rating = int(command[1])

    if plant in info_dict:
        info_dict[plant]['ratings'].append(rating)

    else:
        print('error')

    return info_dict


def update_func(new_command, info_dict):
    command = new_command[1].split(" - ")
    plant = command[0]
    new_rarity = int(command[1])
    if plant in info_dict:
        info_dict[plant]["rarity"] = new_rarity
    else:
        print('error')

    return info_dict


def reset_func(new_command, info_dict):
    plant = new_command[1]

    if plant in info_dict:
        info_dict[plant]['ratings'] = []

    else:
        print('error')

    return info_dict


def plant_discovery():
    numb_plant = int(input())
    info_dict = {}

    for n in range(numb_plant):
        plant, rarity = input().split("<->")
        if plant in info_dict:
            info_dict[plant]["rarity"] += int(rarity)
        else:
            info_dict[plant] = {"rarity": int(rarity), "ratings": []}

    while True:
        command = input()

        if command == 'Exhibition':
            break

        new_command = command.split(": ")
        if new_command[0] == 'Rate':
            info_dict = rate_func(new_command, info_dict)
        elif new_command[0] == 'Update':
            info_dict = update_func(new_command, info_dict)
        elif new_command[0] == 'Reset':
            info_dict = reset_func(new_command, info_dict)

    print("Plants for the exhibition:")

    for key, value in info_dict.items():
        plant = key
        rarity = value['rarity']
        if value['ratings']:
            info_dict[plant]['ratings'] = sum(value['ratings']) / len(value['ratings'])
        else:
            info_dict[plant]['ratings'] = 0

        print(f'- {plant}; Rarity: {rarity}; Rating: {info_dict[plant]["ratings"]:.2f}')


plant_discovery()
