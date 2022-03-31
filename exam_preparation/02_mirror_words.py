import re


def mirror_word():

    text = input()
    pattern = r'([@|#])([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'
    result = re.findall(pattern, text)
    match_words = []

    for match in result:
        if match[1] == match[2][::-1]:
            match_words.append(match[1] + " <=> " + match[2])

    if result:
        print(f"{len(result)} word pairs found!")
    else:
        print("No word pairs found!")
    if not match_words:
        print(f'No mirror words!')
    else:
        print(f'The mirror words are:\n{", ".join(match_words)}')


mirror_word()
