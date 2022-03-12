from anydeck import AnyDeck

cards = AnyDeck()

cards.new_deck(decks=2,
               suits=('Red', 'Blue', 'Yellow', 'Green'),
               cards=('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'))

cards.new_deck(decks=4,
               retain_unused=True,
               wilds='Skip',
               override_defaults=True)

cards.new_deck(decks=8,
               retain_unused=True,
               suits="Wild",
               cards='Wild')

for card in cards.deck:
    print(f'{card.suit} {card.face}')
