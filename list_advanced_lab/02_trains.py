wagons = int(input())
command = input()
train = [0] * wagons
while command != 'End':
    explode = command.split(" ")
    current_command = explode[0]

    if current_command == 'add':
        people = int(explode[1])
        train[-1] += people
    elif current_command == 'insert':
        index = int(explode[1])
        people = int(explode[2])
        train[index] += people
    elif current_command == 'leave':
        index = int(explode[1])
        people = int(explode[2])
        train[index] -= people

    command = input()

print(train)