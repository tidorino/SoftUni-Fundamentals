import re

pattern = r'(w{3}.[A-Za-z0-9-]+(\.[a-z]+)+)'
my_list = []
while True:

    text = input()

    if not text:
        break

    result = re.search(pattern, text)

    if result is not None:
        emails = result.group(1)

        my_list.append(emails)

print("\n".join(my_list))



