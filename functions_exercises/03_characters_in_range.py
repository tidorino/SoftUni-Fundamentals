def char_in_range(letter1, letter2):
    for i in range(ord(letter1) + 1, ord(letter2)):
        print(chr(i), end=" ")


chr1, chr2 = input(), input()
char_in_range(chr1, chr2)

# letter1 = ord(chr1)
# letter2 = ord(chr2)
# list1 = []
# for i in range(letter1 + 1, letter2):
#     list1.append(chr(i))
#
# print(" ".join(list1))