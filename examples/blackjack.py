"""

This is an example of a game using a deck of cards handled by the AnyDeck library.
It's a very simple implementation of a BlackJack game where two hands of two cards
are dealt with one being for the player and other for the dealer. You can hit or
stand. If you draw a card, and it puts you over 21, by checking the total of all
the cards in the players hand, you will 'bust out' and lose. If you stand then the
player total is checked against the total value of the dealers hand to determine a
winner.

*** This file is part of the AnyDeck library examples

"""

from anydeck.anydeck import AnyDeck


def show_hand(current_hand):
    hand_value = 0
    for card in current_hand:
        # Here we are just working with 'Card' attributes
        print(f'{card.face} of {card.suit}\n')
        hand_value += card.value
    return hand_value


# Get a new deck of shuffled cards from AnyDeck
cards = AnyDeck(shuffled=True)

print('   ******* Welcome to the EPIC blackjack simulator *******')
print('   ****** Visit the casino without leaving your IDE ******\n')

# Get two hands of two cards
# draw_hands returns a list of lists of 'Card' objects
# In this case we will use index 0 as the
# player and 1 as the dealer
hand = cards.draw_hand(2, 2, alternating=True)

while True:
    current_value = show_hand(hand[0])

    if current_value > 21:
        print(f'BUSTED as {current_value}!')
        break
    if current_value == 21:
        print('Blackjack!')
        break
    print(f'The current hand totals: {current_value}')

    move = input('(H)it - (S)tand - (C)lose\n')

    if move.lower() == 'h':
        # If the player wants another card just draw() one
        # and append it to your games 'hand' variable
        hand[0].append(cards.draw())
    elif move.lower() == 's':
        print('\nThe Dealer had:\n')
        dealer = show_hand(hand[1])
        if current_value == dealer:
            print('Push')
        elif current_value > dealer:
            print('Winner!')
        else:
            print('You Lose')
        break
    elif move.lower() == 'c':
        break

input('Press enter to exit')
