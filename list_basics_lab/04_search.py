number = int(input())
word = input()
string_list = []
filtered_list = list()

for i in range(number):
    string = input()
    string_list.append(string)
    # string_list.append(input())
    if word in string:
        filtered_list.append(string)

print(string_list)

print(filtered_list)
