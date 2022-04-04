def decrypting_commands(data):

    while True:
        command = input()
        if command == 'Finish':
            break

        new_command = command.split(" ")
        if new_command[0] == 'Replace':
            old_letter = new_command[1]
            new_letter = new_command[2]
            data = data.replace(old_letter, new_letter)
            print(data)
        elif new_command[0] == 'Cut':
            start_index = int(new_command[1])
            end_index = int(new_command[2])
            if 0 < start_index <= end_index <= len(data):
                text_to_remove = data[start_index:end_index + 1]
                data = data[:start_index] + data[end_index + 1:]
                print(data)
            else:
                print(f'Invalid indices!')

        elif new_command[0] == 'Make':
            upper_lower = new_command[1]
            if upper_lower == 'Upper':
                data = data.upper()
                print(data)
            else:
                data = data.lower()
                print(data)

        elif new_command[0] == 'Check':
            string = new_command[1]
            if string in data:
                print(f'Message contains {string}')
            else:
                print(f'Message doesn\'t contain {string}')

        elif new_command[0] == 'Sum':
            start_index = int(new_command[1])
            end_index = int(new_command[2])
            if 0 < start_index <= end_index <= len(data):
                substring = data[start_index:end_index + 1]
                sum_substring = [ord(ch) for ch in substring]
                total_sum = sum(sum_substring)
                print(total_sum)
            else:
                print(f'Invalid indices!')


text = input()
decrypting_commands(text)
