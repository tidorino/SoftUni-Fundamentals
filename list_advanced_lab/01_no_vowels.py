text = input()
vowels = ['a', 'o', 'u', 'e', 'i', 'I']
no_vowels_text = "".join([i for i in text if i not in vowels])
print(no_vowels_text)