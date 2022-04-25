number = int(input())

positives = []
negatives = []
# sum_negatives = 0

for i in range(number):
    current_number = int(input())
    if current_number >= 0:
        positives.append(current_number)
    else:
        negatives.append(current_number)
        # sum_negatives += current_number

print(positives)
print(negatives)
print(f'Count of positives: {len(positives)}')
# print(f'Sum of negatives: {sum_negatives}')
print(f'Sum of negatives: {sum(negatives)}')
