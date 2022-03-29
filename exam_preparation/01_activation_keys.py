activation_key = input()

while True:
    command = input()
    if command == 'Generate':
        break

    new_command = command.split(">>>")
    if new_command[0] == 'Contains':
        substring = new_command[1]
        if substring in activation_key:
            print(f'{activation_key} contains {substring}')
        else:
            print(f'Substring not found!')

    elif new_command[0] == 'Flip':
        upper_lower_letters = new_command[1]
        start_index, end_index = int(new_command[2]), int(new_command[3])
        if upper_lower_letters == 'Upper':
            upper_text = activation_key[start_index:end_index].upper()
            activation_key = activation_key[:start_index] + upper_text + activation_key[end_index:]
            print(activation_key)
        elif upper_lower_letters == 'Lower':
            lower_text = activation_key[start_index:end_index].lower()
            activation_key = activation_key[:start_index] + lower_text + activation_key[end_index:]
            print(activation_key)

    elif new_command[0] == 'Slice':
        start_index, end_index = int(new_command[1]), int(new_command[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)


print(f'Your activation key is: {activation_key}')
