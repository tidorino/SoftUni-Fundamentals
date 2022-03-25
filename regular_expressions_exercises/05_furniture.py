import re


def furniture():

    pattern = r"(?P<item>[a-zA-Z]+)<<(?P<price>\d+|\d+\.\d+)!(?P<number>\d+)"

    sum_furniture = 0
    item_furniture = []
    while True:
        data = input()

        if data == 'Purchase':
            break

        result = re.search(pattern, data)

        if result is not None:
            items = result.group('item')
            price_item = float(result.group('price'))
            numb = float(result.group('number'))

            item_furniture.append(items)
            sum_furniture += price_item * numb

    print('Bought furniture:')

    if sum_furniture > 0:
        print('\n'.join(item_furniture))
    print(f'Total money spend: {sum_furniture:.2f}')


furniture()
