from anydeck.anydeck import AnyDeck

# create three different types of cards that will all be part of a single deck
# This is done by 'retaining' the cards from the last created deck for each new deck

cards = AnyDeck(suits='Weapon',
                cards=('Revolver', 'Rope', 'Wrench', 'Knife', 'Candlestick', 'Lead Pipe'))

cards.new_deck(suits='Person',
               cards=('Mrs White', 'Mrs Peacock', 'Miss Scarlet', 'Professor Plum', 'Mr Green', 'Colonel Mustard'),
               retain_unused=True)

cards.new_deck(suits='Room',
               cards=('Hall', 'Billiard Room', 'Library', 'Lounge', 'Kitchen', 'Dining Room', 'Ballroom', 'Study'),
               retain_unused=True)

# The suit id number is based on the creation of a deck so here we change the suit id based on the suit name
for card in cards.deck:
    if card.suit == 'Person':
        card.suit_id = 2
    if card.suit == 'Room':
        card.suit_id = 3

# Print out the cards in the deck
for i in range(len(cards.deck)):
    print(f'{cards.deck[i].face} ({cards.deck[i].suit})')
