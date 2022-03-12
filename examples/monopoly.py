from anydeck.anydeck import AnyDeck

# Create two independent decks
community_chest_cards = AnyDeck()
chance_cards = AnyDeck()


# Create dictionary of the face and value of the cards
community_chest_dict = {'You Inherit $100': 100,
                        'Doctor\'s Fee Pay $50': -50,
                        'You Won Second Prize in a Beauty Contest Collect $10': 10,
                        'Bank Error in Your Favor': 200,
                        'Get Out of Jail Free': 0}

chance_dict = {'Advance to Boardwalk': 0,
               'Advance to Go': 0,
               'Advance to Illinois Avenue': 0,
               'Bank Pays You Dividends of $10': 10,
               'Speeding Fine $15': 15}

# Create the first deck using a list comprehension that uses the keys from
# the dictionary to populate the card faces
community_chest_cards.new_deck(suits='Community Chest',
                               cards=[card for card in community_chest_dict])

# Pass the dictionary into the dict_t0_value method where the cards with a face
# equals a key will have the value changed based on the dictionary
community_chest_cards.dict_to_value(community_chest_dict)

# Do it again
chance_cards.new_deck(suits='Chance',
                      cards=[card for card in chance_dict])

chance_cards.dict_to_value(chance_dict)

# print out the decks
print(f'{str("Community Chest Card").rjust(55)}     Integer Value')
for com_card in community_chest_cards.deck:
    print(f'{com_card.face.rjust(55)}     {com_card.value}')

print(f'\n{str("Chance Card").rjust(55)}     Integer Value')
for cha_card in chance_cards.deck:
    print(f'{str(cha_card.face).rjust(55)}     {cha_card.value}')
