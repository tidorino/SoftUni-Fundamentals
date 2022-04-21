def phonebook_info(numb_of_lines, phonebook_dict):
    for numb in range(numb_of_lines):
        name = input()
        if name not in phonebook_dict:
            print(f"Contact {name} does not exist.")
        else:
            print(f"{name} -> {phonebook_dict[name]}")

    return True


def phonebook():
    phonebook_dict = {}
    condition = False

    while True:
        info = input().split("-")
        if info[0].isdigit():
            condition = phonebook_info(int(info[0]), phonebook_dict)
        else:
            phonebook_dict[info[0]] = info[1]

        if condition:
            break


phonebook()
