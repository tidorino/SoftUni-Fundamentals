# He'll give you a series of strings (containing only non-numerical characters) followed
# by non-negative numbers (N), e.g., "a3". You need to convert the letters to uppercase
# for each string and print it repeatedly N times on the console. In the example, you need to write
# back "AAA".
# First, on the output, you should print a statistic of the number of unique symbols used
# (case-insensitive) in the format: "Unique symbols used {0}".
# Next, print the rage message itself.
# The strings and numbers will not be separated by anything. The input will always start with
# a non-numeric symbol, and for each string, there will be a corresponding number. The input will
# be given on a single line.

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
