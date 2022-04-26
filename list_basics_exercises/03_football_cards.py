card = input().split(" ")
team_a = 11
team_b = 11
players_loses = []
condition = False

for current_card in card:
    if current_card not in players_loses:
        players_loses.append(current_card)
        if 'A' in current_card:
            team_a -= 1
        elif 'B' in current_card:
            team_b -= 1
        if team_a < 7 or team_b < 7:
            condition = True
            break

print(f'Team A - {team_a}; Team B - {team_b}')

if condition:
    print('Game was terminated')
