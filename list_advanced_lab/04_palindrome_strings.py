list_words = input().split(" ")
palindrome = input()


x = [i for i in list_words if i == "".join(reversed(i))]
y = x.count(palindrome)

print(x)
print(f'Found palindrome {y} times')