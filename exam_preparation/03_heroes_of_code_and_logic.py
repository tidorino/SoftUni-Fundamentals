
number_heroes = int(input())
heroes_dict = {}
hit_points = 100
mana_points = 200

for n in range(number_heroes):
    command = input().split(" ")
    hero_name = command[0]
    hero_hp = int(command[1])
    hero_mp = int(command[2])

    current_hero_dict = {}

    current_hero_dict['hp'] = hero_hp
    current_hero_dict['mp'] = hero_mp
    heroes_dict[hero_name] = current_hero_dict


while True:
    command = input()

    if command == 'End':
        break

    elif 'Heal' in command:
        new_command = command.split(" - ")
        name = new_command[1]
        points_hp = int(new_command[2])

        if heroes_dict[name]['hp'] + points_hp > 100:
            points_hp = 100 - heroes_dict[name]['hp']
            heroes_dict[name]['hp'] = 100
        else:
            heroes_dict[name]['hp'] += points_hp

        print(f'{name} healed for {points_hp} HP!')

    elif 'Recharge' in command:
        new_command = command.split(" - ")
        name = new_command[1]
        points_mp = int(new_command[2])

        if heroes_dict[name]['mp'] + points_mp > 200:
            points_mp = 200 - heroes_dict[name]['mp']
            heroes_dict[name]['mp'] = 200
        else:
            heroes_dict[name]['mp'] += points_mp

        print(f'{name} recharged for {points_mp} MP!')

    elif 'TakeDamage' in command:
        new_command = command.split(" - ")
        name = new_command[1]
        hp_points_to_reduce = int(new_command[2])
        attacker = new_command[3]
        heroes_dict[name]['hp'] -= hp_points_to_reduce

        if heroes_dict[name]['hp'] > 0:

            print(f"{name} was hit for {hp_points_to_reduce} HP by {attacker} "
                  f"and now has {heroes_dict[name]['hp']} HP left!")
        else:
            heroes_dict.pop(name)
            print(f'{name} has been killed by {attacker}!')

    elif 'CastSpell' in command:
        new_command = command.split(" - ")
        name = new_command[1]
        mp_points_needed = int(new_command[2])
        spell_name = new_command[3]

        if heroes_dict[name]['mp'] >= mp_points_needed:
            heroes_dict[name]['mp'] -= mp_points_needed
            # current_points = heroes_dict[name]['mp'] - mp_points_needed

            print(f"{name} has successfully cast {spell_name} and now has {heroes_dict[name]['mp']} MP!")
        else:
            print(f'{name} does not have enough MP to cast {spell_name}!')

for key, value in heroes_dict.items():
    print(key)
    print(f' HP: {value["hp"]}')
    print(f' MP: {value["mp"]}')












