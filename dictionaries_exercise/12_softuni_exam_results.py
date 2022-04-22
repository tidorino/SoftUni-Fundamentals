def exam():
    info_participants = {}
    language_dict = {}
    while True:

        command = input()
        if command == 'exam finished':
            break

        if 'banned' in command:
            command = command.split("-")
            username = command[0]
            del info_participants[username]
            break

        command = command.split("-")
        username = command[0]
        language = command[1]
        points = command[2]

        if username not in info_participants:
            info_participants[username] = [points]
            if language not in language_dict:
                language_dict[language] = 1
            else:
                language_dict[language] += 1
        else:
            info_participants[username] += [points]
            language_dict[language] += 1
    print(f"Results:")

    for key, value in info_participants.items():
        value1 = max(value)
        print(f"{key} | {value1}")
    print(f"Submissions:")

    for key, value in language_dict.items():

        print(f"{key} - {value}")


exam()
