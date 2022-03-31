string = input()

while True:
    command = input()
    if command == "Reveal":
        break

    new_command = command.split(":|:")

    if new_command[0] == "InsertSpace":

        index = int(new_command[1])
        string = string[:index] + ' ' + string[index:]
        print(string)

    elif new_command[0] == "Reverse":
        substring = new_command[1]
        if substring in string:
            string = string.replace(substring, '', 1)
            new_substring = substring[::-1]
            string = string + new_substring
            print(string)
        else:
            print('error')

    elif new_command[0] == "ChangeAll":
        substring = new_command[1]
        replacement = new_command[2]
        string = string.replace(substring, replacement)
        print(string)

print(f"You have a new text message: {string}")
