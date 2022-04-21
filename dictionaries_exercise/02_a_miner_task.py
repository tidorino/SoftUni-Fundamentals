def miner_task():

    resources = {}
    while True:
        command = input()
        if command == 'stop':
            break

        quantity = int(input())
        if command not in resources:
            resources[command] = quantity
        else:
            resources[command] += quantity

    for key, value in resources.items():
        print(f"{key} -> {value}")


miner_task()
