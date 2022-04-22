def items_func(legendary_items_dict, junk_dict, special_item):

    print(f"{special_item} obtained!")
    print(f"shards: {legendary_items_dict['shards']}")
    print(f"fragments: {legendary_items_dict['fragments']}")
    print(f"motes: {legendary_items_dict['motes']}")

    for key, value in junk_dict.items():
        print(f"{key}: {value}")

    return True


def legendary_farming():
    legendary_items_dict = {'shards': 0, 'fragments': 0, 'motes': 0}
    junk_dict = {}
    condition = False

    while True:
        items = input().lower().split(" ")

        for value, material in zip(items[0::2], items[1::2]):
            material = material
            quantity = int(value)

            if material in legendary_items_dict:
                    # ['shards', 'fragments', 'motes']:
                # if material not in legendary_items_dict:
                #     legendary_items_dict[material] = quantity
                # else:
                legendary_items_dict[material] += quantity

                if legendary_items_dict[material] > 250:
                    legendary_items_dict[material] -= 250
                    special_item = ''
                    if material == "shards":
                        special_item = "Shadowmourne"
                    elif material == "fragments":
                        special_item = "Valanyr"
                    elif material == "motes":
                        special_item = "Dragonwrath"

                    items_func(legendary_items_dict, junk_dict, special_item)
                    condition = True

            else:
                if material not in junk_dict:
                    junk_dict[material] = quantity
                else:
                    junk_dict[material] += quantity

            if condition:
                break
        if condition:
            break


legendary_farming()
