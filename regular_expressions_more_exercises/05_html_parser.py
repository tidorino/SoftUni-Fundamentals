import re

html_text = input()

title_regex = r'<title>((?P<title>\w.*)(</title>))'
content_regex = r'<body>((?P<content>\w.*)(</body>))'
content1_regex = r'(?P<first>^\w+)<p>(?P<second>.*)</p>(?P<third>.*)<.*>\\n(?P<forth>.*)'

result_title = re.finditer(title_regex, html_text)
title = ''
for match in result_title:
    title = match.group('title')

result_content = re.finditer(content_regex, html_text)
content = ''
for match in result_content:
    content = match.group('content')

content_list = []
result_final_content = re.finditer(content1_regex, content, re.MULTILINE)

for match in result_final_content:
    first = match.group('first')
    second = match.group('second')
    third = match.group('third')
    forth = match.group('forth')

    content_list.append(first)
    content_list.append(second)
    content_list.append(third)
    content_list.append(forth)
print(f"Title: {title}")
print(f"Content: {''.join(content_list)}")


