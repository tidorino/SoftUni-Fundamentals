number = int(input())

my_list = list()

for i in range(number):
    numb = int(input())
    my_list.append(numb)
    # my_list.append(input())
filter_word = input()
filtered = []

for current_number in my_list:
    if filter_word == 'even' and current_number % 2 == 0:
        filtered.append(current_number)

    if filter_word == 'odd':
        if current_number % 2 != 0:
            filtered.append(current_number)

    if filter_word == 'positive':
        if current_number >= 0:
            filtered.append(current_number)

    if filter_word == 'negative':
        if current_number < 0:
            filtered.append(current_number)


print(filtered)

