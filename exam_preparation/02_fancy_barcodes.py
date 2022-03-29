import re
number = int(input())
pattern = r"(?P<barcode>@#+[A-Z][A-Za-z0-9]+[A-Z]@#+)"

for n in range(number):
    command = input()
    if re.match(pattern, command):
        for match in re.finditer(pattern, command):
            barcode = match.group('barcode')
            new_result = re.findall(r'[0-9]+', barcode)
            if new_result:
                print(f'Product group: {"".join(new_result)}')
            else:
                print(f'Product group: 00')

    else:
        print('Invalid barcode')







