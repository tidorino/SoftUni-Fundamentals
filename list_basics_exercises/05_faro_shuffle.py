cards = input().split(' ')
count_shuffles = int(input())

for num in range(count_shuffles):
    half_cards_length = int((len(cards)) / 2)
    first_deck_of_cards = cards[:half_cards_length]
    second_deck_of_cards = cards[- half_cards_length:]
    cards = []
    for i in range(half_cards_length):
        cards.append(first_deck_of_cards[i])
        cards.append(second_deck_of_cards[i])

print(cards)
