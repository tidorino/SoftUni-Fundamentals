def string_explosion(data):
    data = list(data)
    strength = 0
    index = 0
    for index in range(len(data)):
        if data[index] == '>' and index < len(data) - 1:
            strength += int(data[index + 1])
            while strength > 0 and index < len(data) - 1:
                if not data[index + 1] == '>':
                    index += 1
                    data[index] = 'none'
                    strength -= 1
                else:
                    break

    data = list(filter(lambda x: x != 'none', data))
    print("".join(data))


text = input()
string_explosion(text)
