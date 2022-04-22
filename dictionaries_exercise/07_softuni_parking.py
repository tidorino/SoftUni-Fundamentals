def parking_lot():
    number = int(input())
    register_cars = {}

    for nub in range(number):
        command = input().split(" ")
        name = command[1]

        if command[0] == 'register':
            car_numb = command[2]

            if name not in register_cars:
                register_cars[name] = car_numb
                print(f"{name} registered {car_numb} successfully")
            else:
                print(f"ERROR: already registered with plate number {car_numb}")

        elif command[0] == 'unregister':
            if name not in register_cars:
                print(f"ERROR: user {name} not found")
            else:
                del register_cars[name]
                print(f"{name} unregistered successfully")

    for key, value in register_cars.items():
        print(f"{key} => {value}")


parking_lot()
