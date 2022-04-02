def rage_quit(info):
    info = list(info)
    letters = ''
    new_letters = ''
    unique_symbol = 0
    symbols = ''
    for i in info:

        if i.isdigit():
            new_text = letters * int(i)
            new_letters += new_text
            letters = ''
        else:
            i = i.upper()
            letters += i
            if i not in symbols:
                symbols += i
                unique_symbol += 1

    print(f'Unique symbols used: {unique_symbol}')
    print(new_letters)


string = input()
rage_quit(string)
