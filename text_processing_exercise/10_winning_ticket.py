# You are given a collection of tickets separated by commas and spaces (one or many).
# You need to check each ticket to see if it has a winning combination of symbols:
# •	A valid ticket has exactly 20 characters.
# •	A winning ticket is a valid one, containing one of the symbols '@', '#', '$' or '^'
# uninterruptedly repeated at least 6 times in both halves of the tickets.
# •	In order to win a Jackpot, the ticket should contain the same winning symbol 10 times on both sides


def additional_func(partition):
    current_max_numb = 0
    special_char = ''
    for ch in partition:
        if ch != special_char:
            if current_max_numb >= 6:
                break
            current_max_numb = 1
            special_char = ch
        else:
            current_max_numb += 1

    return [current_max_numb, special_char]


def ticket_validator(ticket):
    ticket_condition = ''

    if len(ticket) != 20:
        ticket_condition = 'invalid ticket'
    elif ticket[0] * 20 == ticket and ticket[0] in '@#$^':
        ticket_condition = f'ticket "{ticket}" - 10{ticket[0]} Jackpot!'
    else:
        data_source = ''
        if additional_func(ticket[0:int(len(ticket) / 2)]) > additional_func(ticket[int(len(ticket) / 2):]):
            data_source = additional_func(ticket[int(len(ticket) / 2):])
        else:
            data_source = additional_func(ticket[0: int(len(ticket) / 2)])
        number_of_special_signs = data_source[0]
        special_sign = data_source[1]

        if number_of_special_signs < 6 or special_sign not in '@#$^':
            ticket_condition = f'ticket "{ticket}" - no match'
        else:
            ticket_condition = f'ticket "{ticket}" - {number_of_special_signs}{special_sign}'

    return ticket_condition


def winning_ticket(data):
    for ticket in data:
        print(ticket_validator(ticket))


info = input()
data = [x.strip() for x in info.split(",")]
winning_ticket(data)
