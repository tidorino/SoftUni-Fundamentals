# numb_list = input().split(" ")
#
# min_numb = min(map(int, numb_list))
# max_numb = max(map(int, numb_list))
# sum_list = sum(map(int, numb_list))
#
# print(f"The minimum number is {min_numb}")
# print(f"The maximum number is {max_numb}")
# print(f"The sum number is: {sum_list}")

def min_max_sum(numbs):
    print(f"The minimum number is {min(numbs)}")
    print(f"The maximum number is {max(numbs)}")
    print(f"The sum number is: {sum(numbs)}")


numbers = list(map(int, input().split(" ")))
min_max_sum(numbers)