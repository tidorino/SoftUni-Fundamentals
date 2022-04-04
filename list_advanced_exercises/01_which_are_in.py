first_text = input().split(", ")
second_text = input()
new_list = [i for i in first_text if i in second_text]


print(new_list)