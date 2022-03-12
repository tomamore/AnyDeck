from anydeck.anydeck import AnyDeck, Card

cards = AnyDeck()

# Create a custom card
old_maid_card = Card(face="Old Maid")

# Add the custom card a 'special card'
# Special Cards are inserted on top of regular cards
cards.new_deck(decks=2,
               cards=('Alto Annie', 'Slap on Sam', 'Billy Blaze', 'Heap Big Talk', 'Clancy Clown', 'Crazy Cop',
                      'Loggin Larry', 'Greenthumb Gert', 'Diver Dan', 'Freddie Falloff', 'Baker Benny',
                      'Tumbledown Tess', 'Hayseed Hank', 'Postman Pete', 'Fifi Fluff', 'Bagpipe Barney', 'Milkman Mo',
                      'Careless Carrie'),
               special_cards=old_maid_card)

# Shuffle the deck
cards.shuffle()

# Draw cards until the deck is empty
while cards.remaining_cards > 0:
    # This is where the card is being drawn
    print(cards.draw().face)
