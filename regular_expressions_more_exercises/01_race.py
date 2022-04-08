def race():
    name = input().split(', ')
    name_list = []
    digit_list = []
    race_participants = {}
    names = ''
    km_run = 0
    while True:
        command = input()
        if command == 'end of race':
            break

        for char in command:
            if char.isalpha():
                name_list.append(char)
            if char.isdigit():
                digit_list.append(int(char))

        names = "".join(name_list)
        km_run = sum(digit_list)
        if names in name:

            if names in race_participants:
                race_participants[names] += km_run
            else:
                race_participants[names] = km_run
            name_list = []
            digit_list = []

    new_dic = {}
    # for n in name:
    #     if n not in race_participants:
    #         race_participants.pop('n')
    # for x in race_participants:
    #     if x in name:
    #         new_dic = race_participants.get(x)


    print(race_participants)


race()