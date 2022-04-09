import re


def bar_incomes():
    pattern = r"^(%(?P<customer>[A-Z][a-z]+)%).*(<(?P<product>\w+)>).*" \
              r"(\|(?P<count>\d+)\|)([^\d]*)((?P<price>\d+(\.\d+)?)\$)$"

    total_price = 0
    while True:
        command = input()
        if command == 'end of shift':
            break

        match = re.match(pattern, command)
        if match:
            name, product = match.group("customer"), match.group("product")
            cost = int(match.group("count")) * float(match.group("price"))
            print(f"{name}: {product} - {cost:.2f}")
            total_price += cost

    print(f'Total income: {total_price:.2f}')


bar_incomes()
