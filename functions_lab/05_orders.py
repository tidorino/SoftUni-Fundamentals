def calculation(product, num):
    if product == 'coffee':
        return num * 1.5
    elif product == 'water':
        return num * 1
    elif product == 'coke':
        return num * 1.4
    elif product == 'snacks':
        return num * 2


current_product = input()
current_num = int(input())
result = calculation(current_product, current_num)
print(f'{result:.2f}')