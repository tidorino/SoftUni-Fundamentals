def add_func(new_command, info_dict):
    piece = new_command[1]
    composer = new_command[2]
    key = new_command[3]
    if piece not in info_dict:
        info_dict[piece] = [composer, key]
        print(f'{piece} by {composer} in {key} added to the collection!')
    else:
        print(f'{piece} is already in the collection!')

    return info_dict


def remove_func(new_command, info_dict):
    piece = new_command[1]
    if piece in info_dict:
        del info_dict[piece]
        print(f'Successfully removed {piece}!')
    else:
        print(f'Invalid operation! {piece} does not exist in the collection.')

    return info_dict


def change_func(new_command, info_dict):
    piece = new_command[1]
    new_key = new_command[2]
    if piece in info_dict:
        info_dict[piece][1] = new_key
        print(f'Changed the key of {piece} to {new_key}!')
    else:
        print(f'Invalid operation! {piece} does not exist in the collection.')

    return info_dict


def pianist():
    numb_pieces = int(input())
    info_dict = {}

    for n in range(numb_pieces):
        command = input().split("|")
        piece = command[0]
        composer = command[1]
        key = command[2]
        info_dict[piece] = [composer, key]

    while True:
        command = input()

        if command == 'Stop':
            break

        new_command = command.split("|")
        if new_command[0] == 'Add':
            info_dict = add_func(new_command, info_dict)
        elif new_command[0] == 'Remove':
            info_dict = remove_func(new_command, info_dict)
        elif new_command[0] == 'ChangeKey':
            info_dict = change_func(new_command, info_dict)

    for data in info_dict:
        piece = data
        composer = info_dict[data][0]
        key = info_dict[data][1]
        print(f'{piece} -> Composer: {composer}, Key: {key}')


pianist()
