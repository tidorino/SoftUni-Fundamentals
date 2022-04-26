day_events = input().split('|')
energy = 100
coins = 100
close_condition = False

for event in day_events:
    current_event = event.split('-')
    type_event = current_event[0]
    number = int(current_event[1])

    if type_event == 'rest':
        if energy >= 100:
            energy = 100
            print(f'You gained 0 energy.')
        else:
            energy += number
            print(f'You gained {number} energy.')

        print(f'Current energy: {energy}.')

    elif type_event == 'order':
        if energy >= 30:
            print(f'You earned {number} coins.')
            coins += number
            energy -= 30

        else:
            energy += 50
            print('You had to rest!')

    else:
        if coins >= number:
            print(f'You bought {type_event}.')
            coins -= number
        else:
            print(f'Closed! Cannot afford {type_event}.')
            close_condition = True
            break

if not close_condition:
    print(f'Day completed!')
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
