def func(number_rooms):
    left_chairs = 0
    condition = True
    for i in range(1, numb_rooms + 1):
        info = input().split(" ")
        visitors = int(info[1])
        chairs = info[0]

        diff = abs(len(chairs) - visitors)

        if visitors > len(chairs):
            condition = False
            print(f'{diff} more chairs needed in room {i}')

        elif len(chairs) > visitors:
            left_chairs += diff

    if condition:
        print(f'Game On, {left_chairs} free chairs left')


numb_rooms = int(input())
func(numb_rooms)