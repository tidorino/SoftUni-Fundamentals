import sys

divisor = int(input())
boundary_number = int(input())
large_number = - sys.maxsize

for i in range(1, boundary_number + 1):
    if i % divisor == 0 and i <= boundary_number:
        if i > large_number:
            large_number = i

print(large_number)