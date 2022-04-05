def perfect_numb(n):
    list_divisors = []
    condition = False
    for i in range(1, n-1):

        if n % i == 0:
            list_divisors.append(i)
            if sum(list_divisors) == n:
                condition = True
                print('We have a perfect number!')

        elif n % i != 0:
            continue

    if not condition:
        print('It\'s not so perfect.')


number = int(input())
perfect_numb(number)