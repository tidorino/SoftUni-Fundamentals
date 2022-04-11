def registration():
    user_name = input()

    while True:
        command = input()
        if command == 'Registration':
            break
        new_command = command.split(" ")

        if new_command[0] == 'Letters':
            lower_upper = new_command[1]
            if lower_upper == 'Lower':
                user_name = user_name.lower()
            else:
                user_name = user_name.upper()
            print(user_name)

        elif new_command[0] == 'Reverse':
            start_index = int(new_command[1])
            end_index = int(new_command[2])
            if 0 < start_index < end_index < len(user_name):
                reversed_text = reversed(user_name[start_index:end_index + 1])
                print(''.join(reversed_text))

        elif new_command[0] == 'Substring':
            substring = new_command[1]
            if substring in user_name:
                user_name = user_name.replace(substring, '')
                print(user_name)
            else:
                print(f"The username {user_name} doesn't contain {substring}.")

        elif new_command[0] == 'Replace':
            char = new_command[1]
            user_name = user_name.replace(char, '-')
            print(user_name)
        elif new_command[0] == 'IsValid':
            char = new_command[1]
            if char not in user_name:
                print(f'{char} must be contained in your username.')
            else:
                print(f'Valid username.')


registration()
