number = float(input())

if number == 0:
    print("zero")
elif 0 < number:
    if number < 1:
        print("small positive")
    elif number > 1000000:
        print("large positive")
    else:
        print("positive")
else:
    if 0 > number:
        if number > - 1:
            print("small negative")
        elif number < - 1000000:
            print("large negative")
        else:
            print("negative")