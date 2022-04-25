string1 = input()
string2 = input()
string3 = input()

meerkats = [string1, string2, string3]

meerkats[0], meerkats[2] = meerkats[2], meerkats[0]

print(meerkats)
