# Write a program that returns an encrypted version of the same text.
# Encrypt the text by replacing each character
# with the corresponding character three positions forward in the ASCII table

def caesar_cipher():
    data = input()
    result = [chr(ord(ch) + 3) for ch in data]
    print("".join(result))


caesar_cipher()
