n = int(input())

sum_characters = 0

for _ in range(n):

    character = input()
    sum_characters += ord(character)

print(f"The sum equals: {sum_characters}")
