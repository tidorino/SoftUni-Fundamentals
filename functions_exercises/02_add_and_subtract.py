def sum_numbers(num1, num2):
    return num1 + num2


def subtract(current_sum, current_c):
    return current_sum - current_c


a, b, c = int(input()), int(input()), int(input())

print(subtract(sum_numbers(a, b), c))