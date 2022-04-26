gifts = input().split(" ")
command = input()

while 'No Money' not in command:
    word = command.split(" ")
    current_command = word[0]
    current_word = word[1]
    if "OutOfStock" in command:
        for i in list(gifts):
            if current_word == i:
                i = 'None'
                res = [item.replace(str(current_word), str(i)) for item in gifts]
                gifts = res.copy()

    elif 'Require' in command:
        gift_index = int(word[2])
        if 0 < gift_index < len(gifts):
            gifts[gift_index] = current_word

    elif 'JustInCase' in command:
        gifts.insert(-1, str(current_word))
        gifts.pop(-1)

    command = input()

for elem in list(gifts):
    if elem == 'None':
        gifts.remove(elem)

print(" ".join(gifts))
