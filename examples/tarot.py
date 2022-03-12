from anydeck import AnyDeck, Card

cards = AnyDeck(suits='Tarot',
                cards=('Strength', 'The Moon', 'Justice', 'The Hermit', 'The Fool', 'The Sun', 'The Tower',
                       'Temperance'))

# Draw all cards in the deck and print them as they are drawn from the deck
for _ in range(len(cards.deck)):
    card = cards.draw()
    print(f'You have drawn *{card.face}*')

# Replace the cards that we drew for the used pile (in this case all of them)
cards.replace_used_cards()

# Create a Card object
card = Card(face='The Jester',
            suit='Tarot')

# Add the created Card to the top of now replaced deck.
cards.add_card(card, position='top')

print()
# Draw all cards in the deck and print them which now includes the added card
for _ in range(len(cards.deck)):
    card = cards.draw()
    print(f'You have drawn *{card.face}*')
