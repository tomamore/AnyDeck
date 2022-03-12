from anydeck import AnyDeck

# Please forgive this sloppy mess. It's meant to be run and the code worked through while
# seeing the values assigned to the cards. I tried to keep the code simple to make following
# along easier.

# Create a parent deck of 2 identical decks
cards = AnyDeck(decks=2)

# Print out all the cards and some card attributes. This is meant as a visualization
# of how the cards are ordered by the library.

for card in cards.deck:
    print(f'{(card.face + " of " + card.suit).rjust(20)} - '
          f'Value {str(card.value).rjust(2)} - '
          f'Child Deck Order # {str(card.child_order_num).rjust(2)} - '
          f'Suit Order # {str(card.suit_order_num).rjust(2)} - '
          f'Unique Card # {str(card.unique_card_num).rjust(3)} - '
          f'Suit Id # {str(card.suit_id)} - '
          f'Child Deck # {str(card.child_deck_num)}')
    if card.value == 11 and card.unique_card_num < cards.total_cards and card.child_order_num % 52 != 0:
        print('\n                     @@@@@@@@@@@@@@@@@@@ Next Suit in Child Deck @@@@@@@@@@@@@@@@@@@\n')
    if card.child_order_num % 52 == 0 and card.unique_card_num < cards.total_cards:
        print('\n                     ***************** NEXT CHILD DECK *****************\n')

print('\n****Deck Information stored at deck creation*****\n')

# Finally, print out the information about deck
for k, v in cards.get_deck_info().items():
    print(k, v)


# Create a small deck with jokers
cards = AnyDeck(decks=2, cards=['2', '3', '4'], suits=['squares', 'circles'], wilds=2)

# Notice how wild cards are given a suit id and order of 0 as they do not belong to the
# regular suits. By default, they have a suit name of 'Wild'. Their child deck order number will begin
# after the regular cards are added.

print('\n****Let\'s add some jokers*****')
print('\n------------------------------------------------------------------------------------')
print('-                                        Default Values                            -')
print('------------------------------------------------------------------------------------\n')

for card in cards.deck:
    print(f'{(card.face + " of " + card.suit).rjust(20)} - '
          f'Value {str(card.value).rjust(2)} - '
          f'Child Deck Order # {str(card.child_order_num).rjust(2)} - '
          f'Suit Order # {str(card.suit_order_num).rjust(2)} - '
          f'Unique Card # {str(card.unique_card_num).rjust(3)} - '
          f'Suit Id # {str(card.suit_id)} - '
          f'Child Deck # {str(card.child_deck_num)}')

# Let us loop through the wild cards and make some adjustments
for card in cards.deck:
    if card.suit == 'Wild':
        card.value = 9
        card.suit = 'Others'

print('\n------------------------------------------------------------------------------------')
print('-                             After Adjusting Wild Values                          -')
print('------------------------------------------------------------------------------------\n')

for card in cards.deck:
    print(f'{(card.face + " of " + card.suit).rjust(20)} - '
          f'Value {str(card.value).rjust(2)} - '
          f'Child Deck Order # {str(card.child_order_num).rjust(2)} - '
          f'Suit Order # {str(card.suit_order_num).rjust(2)} - '
          f'Unique Card # {str(card.unique_card_num).rjust(3)} - '
          f'Suit Id # {str(card.suit_id)} - '
          f'Child Deck # {str(card.child_deck_num)}')

# Let's remove all the cards with the 'square' suit
for card in [card for card in reversed(cards.deck)]:
    if card.suit == 'squares':
        cards.deck.remove(card)

print('\n------------------------------------------------------------------------------------')
print('-                                After Removing Squares                            -')
print('------------------------------------------------------------------------------------\n')

for card in cards.deck:
    print(f'{(card.face + " of " + card.suit).rjust(20)} - '
          f'Value {str(card.value).rjust(2)} - '
          f'Child Deck Order # {str(card.child_order_num).rjust(2)} - '
          f'Suit Order # {str(card.suit_order_num).rjust(2)} - '
          f'Unique Card # {str(card.unique_card_num).rjust(3)} - '
          f'Suit Id # {str(card.suit_id)} - '
          f'Child Deck # {str(card.child_deck_num)}')
