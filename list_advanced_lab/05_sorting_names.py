names = input().split(", ")
sorted_names = sorted(names)
new_line = sorted(sorted_names, key=lambda x: -len(x))
print(new_line)
