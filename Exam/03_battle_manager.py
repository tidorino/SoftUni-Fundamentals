def battle_manager():

    info_dict = {}
    count_people_left = 0
    while True:
        command = input()
        if command == 'Results':
            break

        new_command = command.split(":")

        if new_command[0] == 'Add':
            name = new_command[1]
            health = int(new_command[2])
            energy = int(new_command[3])
            if name not in info_dict:
                info_dict[name] = [health, energy]
                count_people_left += 1
            else:
                info_dict[name][0] += health

        elif new_command[0] == 'Attack':
            attacker_name = new_command[1]
            defender_name = new_command[2]
            damage = int(new_command[3])
            if attacker_name in info_dict and defender_name in info_dict:
                info_dict[defender_name][0] -= damage
                info_dict[attacker_name][1] -= 1
                if info_dict[defender_name][0] <= 0:
                    info_dict.pop(defender_name)
                    count_people_left -= 1
                    print(f'{defender_name} was disqualified!')

                if info_dict[attacker_name][1] <= 0:
                    info_dict.pop(attacker_name)
                    count_people_left -= 1
                    print(f'{attacker_name} was disqualified!')

        elif new_command[0] == 'Delete':
            name = new_command[1]
            if name == 'All':
                count_people_left = 0
                info_dict.clear()

            elif name in info_dict:
                count_people_left -= 1
                info_dict.pop(name)

    print(f'People count: {count_people_left}')
    for person in info_dict:
        print(f'{person} - {info_dict[person][0]} - {info_dict[person][1]}')


battle_manager()
