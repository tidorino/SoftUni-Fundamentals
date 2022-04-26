numbers = input().split(" ")
copy_numbs = list(map(int, numbers))
numbers_to_remove = int(input())

for i in range(numbers_to_remove):
    current_num = min(copy_numbs)
    numbers.remove(str(current_num))
    copy_numbs.remove(current_num)

print(", ".join(numbers))
