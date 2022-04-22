def product_func(product_dict, items):

    name = items[0]
    price = float(items[1])
    quantity = int(items[2])

    if name in product_dict:
        product_dict[name] = [price, (quantity + product_dict[name][1])]
    else:
        product_dict[name] = [price, quantity]

    return product_dict


def orders():

    product_dict = {}

    while True:
        command = input()

        if command == 'buy':
            break

        command = command.split(" ")
        product_dict = product_func(product_dict, command)

    for i in product_dict:
        total_sum = product_dict[i][0] * product_dict[i][1]
        print(f"{i} -> {total_sum:.2f}")


orders()
