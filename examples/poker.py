from anydeck.anydeck import AnyDeck

# Create a shuffled deck with 2 wild cards with a face of 'Joker'
cards = AnyDeck(shuffled=True, wilds=['Joker', 'Joker'])

hand = []

# Draw 5 cards and put them in the hand array
for _ in range(5):
    hand.append(cards.draw())

# Print each card in the hand deck
print(
    f'                  ************** DRAWN HAND **************\n'
    f'{hand[0].face} of {hand[0].suit}     '
    f'{hand[1].face} of {hand[1].suit}     '
    f'{hand[2].face} of {hand[2].suit}     '
    f'{hand[3].face} of {hand[3].suit}     '
    f'{hand[4].face} of {hand[4].suit}\n')

# Alternatively use draw_hand:

# Creating a new AnyDeck default set. Notice that shuffled was not set to True.
# With an ordered deck we can see the alternating feature of the draw_hand method below.
cards = AnyDeck(shuffled=True)

# draw_hands returns a list of cards per hand (x, y). Alternating draws a card to each hand before
# continuing with the next card for each hand. Refill begins with the used pile, which is shuffled,
# and when that is exhausted a new shuffled deck is created from a duplicate of the original deck
# and the dealing continues.
hands = cards.draw_hand(5, 2, alternating=False, refill=False)

print(f'                  ************** DRAWN HANDS **************')
for hand in hands:

    # Print each card in the hand deck
    # For the simplicity of this example a deck of 5 cards is shown
    # Fell free to play with the number of hands above.
    print(
        f'{hand[0].face} of {hand[0].suit}      '
        f'{hand[1].face} of {hand[1].suit}      '
        f'{hand[2].face} of {hand[2].suit}      '
        f'{hand[3].face} of {hand[3].suit}      '
        f'{hand[4].face} of {hand[4].suit}')
