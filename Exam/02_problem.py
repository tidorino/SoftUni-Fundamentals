import re

numb_strings = int(input())

for n in range(numb_strings):
    text = input()
    command = r'(!)([A-Z][a-z]{2,})\1'

    string = r'\[[a-zA-Z]{8,}\]'
    match_command = re.finditer(command, text)

    for com in match_command:
        if com[2] in text:
            match_string = re.finditer(string, text)
            for i in match_string:
                if i[0] in text:
                    text_numb = str([ord(ch) for ch in i[0]])
                    total_n = "".join(text_numb)
                    print(f'{com[2]}: {total_n}')
                else:
                    print('The message is invalid')

    else:
        print('The message is invalid')