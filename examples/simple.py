from anydeck import AnyDeck

# Create a default deck
# A default deck consists of a standard deck of poker cards with four suits with cards numbered 2 through 10, as well
# as a Jack, Queen, King, and Ace for each suit. The standard deck gives a value to the card equal to their
# face value further Jack, Queen, and King have a value of 10 and Ace has a value of 11.
cards = AnyDeck()

# Draw a card from the top (the default for a draw)
card = cards.draw()

# Print the card
print(f'{card.face} of {card.suit}')

# Draw a card from the bottom
card = cards.draw(position='bottom')

# Print the card
print(f'{card.face} of {card.suit}')


# Recreate a new standard deck; this time shuffled
cards = AnyDeck(shuffled=True)

# Draw a card from the top
card = cards.draw()

# Print the card
print(f'{card.face} of {card.suit}')

# Draw another card from the top
card = cards.draw()

# Print the card
print(f'{card.face} of {card.suit}')
