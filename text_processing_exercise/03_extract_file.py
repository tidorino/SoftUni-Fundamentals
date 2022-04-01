# Write a program that reads the path to a file and subtracts the file name and its extension.

text = input().split("\\")
file_name = text[-1].split(".")
file_name1 = file_name[0]
extension = file_name[1]
print(f"File name: {file_name1}")
print(f"File extension: {extension}")
