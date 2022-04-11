import re

number = int(input())
count = 0
for n in range(number):
    data = input()
    pattern = r'U\$([A-Z][a-z]{2,})U\$P@\$([A-Za-z]{5,}[0-9]+)P@\$'

    matches = re.search(pattern, data)
    if matches:
        username = matches.group(1)
        password = matches.group(2)
        count += 1
        print('Registration was successful')
        print(f'Username: {username}, Password: {password}')

    else:
        print('Invalid username or password')

print(f'Successful registrations: {count}')
