from anydeck import AnyDeck

cards = AnyDeck()

# Adding 'wild' cards
# Wild Cards are inserted after the regular cards and are repeated for each child deck.
# Wild cards can be a single string, a list of strings, or an integer. If an integer is passed
# you will end up with that many cards with a face of 'Joker'
cards.new_deck(suits=('Red', 'Blue', 'Yellow', 'Green'),
               cards=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                      '1', '2', '3', '4', '5', '6', '7', '8', '9',
                      'Skip', 'Draw 2', 'Reverse', 'Skip', 'Draw 2', 'Reverse'),
               wilds=('Wild', 'Wild', 'Wild', 'Wild',
                      'Draw 4', 'Draw 4', 'Draw 4', 'Draw 4'))

# Note that we are not drawing the cards only printing the deck
for card in cards.deck:
    print(f'{str(card.suit).rjust(7)}  {card.face}')
