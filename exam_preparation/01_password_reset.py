text = input()

while True:
    command = input()
    new_list =[]
    if command == "Done":
        break
    new_command = command.split(" ")

    if command == 'TakeOdd':
        text = text[1::2]
        print(text)

    elif new_command[0] == 'Cut':
        index, lenght = int(new_command[1]), int(new_command[2])
        text = text[:index] + text[index + lenght:]
        print(text)

    elif new_command[0] == 'Substitute':
        substring, substitute = new_command[1], new_command[2]
        if substring in text:
            text = text.replace(substring, substitute)
            print(text)
        else:
            print("Nothing to replace!")

print(f'Your password is: {text}')

