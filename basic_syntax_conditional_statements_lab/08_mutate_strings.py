first_text = input()
second_text = input()

for i in range(len(first_text)):
    if first_text[i] != second_text[i]:

        final_word = second_text[i]
        word = first_text[0:i] + final_word + first_text[i + 1:]
        first_text = word
        print(first_text)