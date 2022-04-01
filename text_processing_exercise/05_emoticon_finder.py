# Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.

import re


def emoticon_finder(data):
    # pattern = r':.'
    # result = re.findall(pattern, data)
    # for match in result:
    #     print(match)
    result = [data[i] + data[i+1] for i in range(len(data)) if data[i] == ":" and data[i + 1] != " "]
    print("\n".join(result))


info = input()
emoticon_finder(info)
