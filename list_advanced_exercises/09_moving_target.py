numbers = list(map(int, input().split(" ")))
command = input()

while command != 'End':
    new_command = command.split(" ")
    comm = new_command[0]
    i = int(new_command[1])
    y = int(new_command[2])

    if comm == 'Shoot':
        if 0 <= i < len(numbers):
            if (numbers[i] - y) <= 0:
                numbers.remove(numbers[i])
            else:
                numbers[i] -= y

    elif comm == 'Add':
        if 0 <= i < len(numbers):
            numbers.insert(i, y)
        else:
            print('Invalid placement!')

    elif comm == 'Strike':
        if i - y >= 0 and i + y < len(numbers):
            numbers = numbers[:i-y] + numbers[i+y+1:]
        else:
            print("Strike missed!")
            break

    command = input()

new_numbers = list(map(str, numbers))
print("|".join(new_numbers))