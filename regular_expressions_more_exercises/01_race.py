import re


def race():
    name = input().split(', ')
    race_participants = {}

    while True:
        command = input()
        if command == 'end of race':
            break

        pattern = r"([A-Za-z])"
        result = re.findall(pattern, command)
        result_name = "".join(result)

        dijit_pattern = r"([0-9])"
        new_result = re.findall(dijit_pattern, command)
        new_result = "".join(new_result)
        result_dijit = sum(list(map(int, new_result)))

        if result_name not in race_participants and result_name in name:
            race_participants[result_name] = result_dijit
        elif result_name in race_participants:
            race_participants[result_name] += result_dijit

    race_participants = sorted(race_participants.items(), key=lambda item: -item[1])
    new_race_part = race_participants[:3]

    print(f"1st place: {new_race_part[0][0]}")
    print(f"2nd place: {new_race_part[1][0]}")
    print(f"3rd place: {new_race_part[2][0]}")


race()
