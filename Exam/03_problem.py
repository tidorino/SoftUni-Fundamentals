def hero_recruitment():

    heroes = {}
    while True:
        command = input()
        if command == 'End':
            print('Heroes:')
            break
        new_command = command.split(" ")

        if new_command[0] == 'Enroll':
            hero_name = new_command[1]
            if hero_name not in heroes:
                heroes[hero_name] = {}
            else:
                print(f'{hero_name} is already enrolled.')

        elif new_command[0] == 'Learn':
            hero_name = new_command[1]
            spell_name = new_command[2]
            if hero_name in heroes:

                if spell_name in heroes[hero_name].values():
                    print(f'{hero_name} has already learnt {spell_name}.')

                else:
                    heroes[hero_name]['spell'] = spell_name

            else:
                print(f"{hero_name} doesn't exist.")

        elif new_command[0] == 'Unlearn':
            hero_name = new_command[1]
            spell_name = new_command[2]
            if hero_name in heroes:
                if spell_name not in heroes[hero_name]:
                    print(f"{hero_name} doesn't know {spell_name}.")
                else:
                    del heroes['spell']
            else:
                print(f"{hero_name} doesn't exist.")

    for key, value in heroes.items():
        spell = "".join(value.values())
        print(f'== {key}: {spell}')


hero_recruitment()

