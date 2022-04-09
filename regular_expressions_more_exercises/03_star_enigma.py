# You will receive several messages, which are encrypted using the legendary star enigma.
# You should decrypt the messages, following these rules:
# To properly decrypt a message, you should count all the letters [s, t, a, r] – case insensitive
# and remove the count from the current ASCII value of each symbol of the encrypted message.
# After decryption:
# Each message should have a planet name, population, attack type ('A', as attack or 'D',
# as destruction) and soldier count.
# The planet name starts after '@' and contains only letters from the Latin alphabet.
# The planet population starts after ':' and is an Integer;
# The attack type may be "A"(attack) or "D"(destruction) and must be surrounded by "!" (exclamation mark).
# The soldier count starts after "->" and should be an Integer.
# The order in the message should be: planet name -> planet population -> attack type -> soldier count.
# Each part can be separated from the others by any character except: '@', '-', '!', ':' and '>'.
#  InPut : 2
# STCDoghudd4=63333$D$0A53333
# EHfsytsnhf?8555&I&2C9555SR

# 60/ 100 v Judge!

import re

number = int(input())
count = 0

planet_a = []
planet_d = []
for n in range(number):
    count = 0
    regex = r"[s,t,a,r,S,T,R,A]"
    test_str = input()
    matches = re.finditer(regex, test_str)
    for matchNum, match in enumerate(matches, start=1):
        count += 1
    my_list = []
    for i in range(len(test_str)):
        if i < len(test_str):

            letter = chr(ord(test_str[i]) - count)
            my_list.append(letter)
    message = "".join(my_list)

    regex1 = r"@(?P<planet>[A-Za-z]+).*\:(?P<population>\d+)\!(?P<attack_type>[AD])!->(?P<soldiers>\d+)"
    matches = re.finditer(regex1, message)

    for match in matches:
        if match.group('attack_type') == 'A':

            planet_a.append(match.group('planet'))

        else:

            planet_d.append(match.group('planet'))
planet_a = sorted(planet_a)
planet_d = sorted(planet_d)

print(f'Attacked planets: {len(planet_a)}')
for name in planet_a:
    print(f"-> {name}")

print(f'Destroyed planets: {len(planet_d)}')
for name in planet_d:
    print(f"-> {name}")








