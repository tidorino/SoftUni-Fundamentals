''' Create a program that receives two strings on a single line separated by a single space.
# Then, it prints the sum of their multiplied character codes as follows: multiply str1[0] with str2[0] and
# add the result to the total sum, then continue with the next two characters.
# If one of the strings is longer than the other, add the remaining character codes to the total sum
# without multiplication '''


def sum_func(str1, str2):
    total_sum = 0

    for i in range(len(str1)):
        if i < len(str2):
            total_sum += ord(str1[i]) * ord(str2[i])
        else:
            total_sum += ord(str1[i])

    return total_sum


def character_multiplier(data):
    str1 = data[0]
    str2 = data[1]
    result = 0

    if len(str1) > len(str2):
        result = sum_func(str1, str2)
    else:
        result = sum_func(str2, str1)

    print(result)


text = input().split(" ")
character_multiplier(text)

