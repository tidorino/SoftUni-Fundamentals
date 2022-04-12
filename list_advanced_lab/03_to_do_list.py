todo = ["" for i in range(11)]

command = input()

while command != 'End':
    new_command = command.split("-")
    numb = new_command[0]
    text = new_command[1]
    todo[int(numb)] = text

    command = input()

final_todo = [y for y in todo if y != ""]
print(final_todo)