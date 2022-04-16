orders = int(input())

total = 0

for i in range(1, orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())
    order_price = capsules_count * days * price_per_capsule
    total += order_price
    print(f"The price for the coffee is: ${order_price:.2f}")

print(f"Total: ${total:.2f}")