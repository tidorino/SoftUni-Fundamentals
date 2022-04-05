def palindrome_numbs(numbs):
    for num in numbs:
        # if num == "".join(reversed(num))
        if num == num[::-1]:
            print(True)
        else:
            print(False)


numbers = input().split(", ")
palindrome_numbs(numbers)