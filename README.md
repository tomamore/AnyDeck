### Definitions:

* **Special Cards**: One off cards that are added to the parent deck
* **Wild Cards**: Added to the end of each child deck
* **Child Deck**: An indivivual deck of regular and wild cards
* **Parent Deck**: The all encompassing deck that you will ultimently interact with. Includes all child decks and special cards
				   
### Order of Card Insertion at Deck Creation:
1. Retained, unused, cards
2. Special Cards
3. Regular Cards
4. Wild Cards

### Deck Creation:
The simplest implementation is to simply call the library. With this call you will have a standard deck of 52 cards in a list of 'Card' objects refered to as the 'deck'.

``` python
    cards = AnyDeck()
```
Now let's take a look at the deck...
``` python
    for card in cards.deck:
        print(f'{card.face} of {card.suit}')
```
		
Notice that the cards are not shuffled. Shuffeling can be handled in two ways.

* During initization of the the deck

``` python
    cards = AnyDeck(shuffled=True)
```
* At any time
``` python
    cards.shuffle()
```

Instead of using the default cards you can get a _custom deck_ of regular cards by passing arguments.

For example:

1. Create a deck of cards for the faces listed in 'cards'. A card will be created for each card in each suit provided. In this case a deck will be created with 8 cards, all with the suit of 'Tarot'

``` python
    cards = AnyDeck(suits='Tarot',
                    cards=('Strength', 'The Moon', 'Justice', 'The Hermit', 'The Fool', 
                    'The Sun', 'The Tower', 'Temperance'))
```

2. Create a set of multiple decks of regular cards added into one parent deck. The following will yield a deck of 96 cards numbered 1 to 12 for each suit provided for the number of decks provided.
``` python
    cards.new_deck(decks=2,
                   suits=('Red', 'Blue', 'Yellow', 'Green'),
                   cards=('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'))
```
3. Let's do that again but with some wild cards. This time each child deck contains a 'wild' card with a face of 'Skip'.
       This results in a deck of 98 cards. The same as before but with two skips cards (one for each child deck).
``` python
    cards.new_deck(decks=2,
                   suits=('Red', 'Blue', 'Yellow', 'Green'),
                   cards=('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'),
                   wilds='Skip')
```
4. Let's add a total of 4 'Skip' cards and 8 'Joker' cards to the original deck. In this case we will utilize the 'retain' argument of the new_deck method.

   * First, we create the base deck of 96 cards:
        ``` python
            cards.new_deck(decks=2,
                           suits=('Red', 'Blue', 'Yellow', 'Green'),
                           cards=('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')) 
        ```

   * Now we can add the 'Skip' cards by retaining the original deck and adding the new deck into it by creating four child decks with a face of 'Skip' and a suit of 'Wild'. Since we passed the suits and cards arguments the default cards will not be generated. When the new_deck is generated it will retain the cards created from the first deck due to the retain flag being True.
        ``` python
            cards.new_deck(decks=4,
                           retain_unused = True,
                           suits='Wild',
                           cards='Skip')  
        ```
   
   * Finally, to add the eight jokers we do the same thing again. This time though we will simply override the adding of the default cards so that we can make a deck of eight children decks (each consisting of a single card) and again using the retain deck to keep all of the already generated cards.
        ``` python
            cards.new_deck(decks=8
                           retain_unused = True,
                           wilds='Joker',
                           override_defaults=True)
        ```
   * Notice that what we did was first create a deck of 96 standard cards, and then a deck of 4 'Skip' cards, and finally a deck of 8 'Joker' cards. Using retain we kept the cards from each deck as a new deck was added so we end up with a deck of 108 cards. This is the same as....
        ``` python
               cards.new_deck(decks=2,
                              suits=('Red', 'Blue', 'Yellow', 'Green'),
                              cards=('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'),
                              wilds=('Skip', 'Skip', 'Joker', 'Joker', 'Joker, 'Joker')
        ```

      ....since each child deck gets one of each wild card provided to the argument. Thus, each child deck would have 2 Skip and 4 Joker cards. With that we would end up with the same 108 cards only in a slightly different order (see 'Order of card insertion at deck creation')


5. "Special Cards" are passed as Card objects and are added to the top of the deck regardless of the amount of child decks added. In this example a special card with just the face value of "Old Main" is created and then passed to the new_deck method. This example will create the special card and then two decks of regular cards that were added by face.
``` python
    old_maid_card = Card(face="Old Maid")

    cards.new_deck(decks=2,
                   cards=('Alto Annie', 'Slap on Sam', 'Billy Blaze', 'Heap Big Talk', 'Clancy Clown', 'Crazy Cop',
                          'Loggin Larry', 'Greenthumb Gert', 'Diver Dan', 'Freddie Falloff', 'Baker Benny',
                          'Tumbledown Tess', 'Hayseed Hank', 'Postman Pete', 'Fifi Fluff', 'Bagpipe Barney',
                          'Milkman Mo', 'Careless Carrie'),
                   special_cards=old_maid_card)
```
### Drawing Cards:
There are two main ways to draw cards.

1. A single card draw is done simply with:
```python
   card = cards.draw()
```
* This will return a single card object from the top of the deck. See the method arguments for more information of where in the deck the card should come from.


2. Multiple complete hands can be drawn at once with a single statement. The amount of cards in the hand is required. In
   this case the hand size is 5 cards.
```python
   card = cards.draw_hand(5)
```
* A call to this method will return a list containing lists of cards. Further arguments can produce more than one hand, choose to alternate the dealing of the cards, and handle situations where the deck has run out. Refer to the Classes and Methods section.

### Replacing Used Cards:
At any time, the cards which have already been drawn can be return to the bottom of the deck with:
```python
   cards.replace_used_cards()
```

The default behavior is not to shuffle the cards but to simply place them back into the deck. An argument can be
pass to shuffle the used pile before putting the cards on the bottom as well as shuffling the entire deck after
replacing the used cards. Refer to the Classes and Methods section.

### Replacing card values from a dictionary:
Card values can be set by referring  to a dictionary passed to the dict_to_value method. A dictionary with keys equal to the face of the cards and values equal to the int value of the card is required.
```python
   community_chest_cards = AnyDeck()

   community_chest_dict = {'You Inherit $100': 100,
                           'Doctor\'s Fee Pay $50': -50,
                           'Get Out of Jail Free': 0}

   community_chest_cards.new_deck(suits='Community Chest',
                                  cards=[card for card in community_chest_dict])

   community_chest_cards.dict_to_value(community_chest_dict)
```
The above uses a comprehension to create the list of cards to be created in the new deck. Next the dict_to_value
method is called with the dictionary which will set the cards to the values listed in the dictionary.


## Class - Card:
### Attributes:

* **face:** (str) The human readable text of a card (ie: "2" or "Ace") (Default - None)
* **suit:** (str) The human readable text of a card suit (ie: "Spades" or "Red") (Default - None)
* **value:** (int) Value assigned to card (Default - 0)
* **suit_id:** (int) Key sequentially assigned to suits as they are added to a deck (Default - 0)
* **suit_order_num:** (int) The order of the card in the suit it belongs to (Default - 0)
* **child_order_num:** (int) The order of the card in the child deck (Default - None)
* **unique_card_num:** (int) Unique number assigned to each card as they are added to the deck (Default - None)
* **child_deck_num:** (int) The sequence number of the child deck (Default - None)

## Class - AnyDeck:
###**Attributes**

* **total_cards:** (int) Returns the amount of cards which encompass the entire deck at creation
* **remaining_cards:** (int) Returns the amount of cards remaining in the deck
* **deck_info:** (dict) Returns a dictionary with information about the total deck

### Methods:
### \_\_inti\_\_:
During the initialization of the library the arguments are passed to the new_deck function. If the library is called without cards and suits then a default deck will be generated which includes a standard deck of US playing cards.
    
**Arguments:**

                    decks:  (int) The number of duplicate decks to compile into the parent deck (Default - 1)
                 shuffled: (bool) Should the deck be shuffled (Default - False)
                    wilds: (list) Strings in the list will be added as 'face' to wild cards (Default - None)
                            (str) String will be added as 'face' to the wild card (Default - None)
                            (int) Will create int number of wild cards with the 'face' of 'Wild' (Default - None)
                    suits: (list) Strings in the list will be added as suits in the regular deck (Default - None)
                            (str) String will be added as the only suit in the regular deck (Default - None)
                    cards: (list) Strings in the list will be added as cards in the regular deck (Default - None)
                            (str) String will be added as the only card in the regular deck (Default - None)
            special_cards: (Card) One off special cards to be added to the parent deck
        override_defaults: (bool) Allows you to override adding the default cards and suits so that only
                                  special or wild cards are added to the deck without any regular cards. (Default - False)

### new_deck:
Creates a new deck of cards from the provided arguments. If no cards and no suits are provided then a default deck
of 2 through 10, Jack, Queen, King and Ave is generated. Wild and special cards can be added to a default deck. If
you instead need a deck with no regular cards you can call 'override_defaults'. The retain arguments will allows for
keeping cards between cards to new_deck. Used cards are cards which have already been drawn from the deck. Retaining
used cards will simply maintain the used pile. Unused cards are cards which are still in the deck when new_deck is
called. Retaining unused cards are kept at the top of the deck and any new cards are added to the bottom of the unused
cards. Note that wild cards are added with a default suit of 'Wild' and a value of 0.

**Arguments:**

                decks:  (int) The number of duplicate decks to compile into the parent deck (DEFAULT = 1)
             shuffled: (bool) Should the deck be shuffled (DEFAULT = False)
                wilds: (list) Strings in the list will be added as 'face' to wild cards (DEFAULT = None)
                        (str) String will be added as 'face' to the wild card (DEFAULT = None)
                        (int) Will create int number os wild cards with the 'face' of 'Wild' (DEFAULT = None)
                suits: (list) Strings in the list will be added as suits in the regular deck (DEFAULT = None)
                        (str) String will be added as the only suit in the regular deck (DEFAULT = None)
                cards: (list) Strings in the list will be added as cards in the regular deck (DEFAULT = None)
                        (str) String will be added as the only card in the regular deck (DEFAULT = None)
        special_cards: (Card) One off special cards to be added to the parent deck
    override_defaults: (bool) Allows you to override adding the default cards and suits so that only
                              special or wild cards are added to the deck without any regular cards. (DEFAULT = False)
        retain_unused:
          retain_used:
**Returns:**

		Nothing
---
### draw:
Returns a Card object from the deck from the argument provided position. When a card is drawn it is added to the internal
'used_cards' list. At the application level the card does not have to be returned to be considered 'used'.

**Arguments:**

		position: (int) Returns card from the index position of the currently unused deck
                      (str) Returns card from named position (DEFAULT = 'top')
                            ('random') Returns card from a random position of the currently unused deck
                            ('top') Returns card from the top of the unused deck
                            ('bottom') Returns card from the bottom of the unused deck
                            ('middle) Returns card from the middle of the unused deck

**Returns**:	
		
		Nothing
---
### draw_hand:
Draws multiple cards into individual hands based on the arguments provided. Arguments will allow an alternating
drawn where each hand is given a card in turn as opposed to each hand being given all cards before moving on
to the next hand. Should the unused deck run out of cards the refill argument can be set to add the used cards back into
the active deck to continue dealing the required number of cards upon unused completion. Further, with refill set,
a new deck will be created that was identical to the original deck and dealing will continue should all cards be
drawn. Should refill be set to false then the cards will be drawn until the used cards are depleted and the returned
list will have only the cards left in order of the other arguments.

**Arguments**:

             cards:   (int)  REQUIRED: number of cards requested for each hand
             hands:   (int)  Number of hands requested (DEFAULT = 1)
       alternating:  (bool)  (DEFAULT = True)
                     (True)  Draws cards through alternating hands before beginning  the first deck again
                    (False)  Draws all cards to a hand before moving on to subsequent hands
            refill:  (bool)  (DEFAULT = True)
                             (True) Refill the deck if there are not enough cards to complete the draw
                             (False) Returns the list up until that last available card

**Returns:**	
		
		List of Lists of Cards
---
### add_card:
Add a Card object to the deck from the argument provided position.

**Arguments:**

            card: (Card) REQUIRED: Card object to be added
        position:  (int) Add card to the index position of the currently unused deck
                   (str) (DEFAULT = 'bottom')
                         ('random') Add card to a random position of the currently unused deck
                         ('top') Add card to the top of the unused deck
                         ('bottom') Add card to the bottom of the unused deck
                         ('middle) Add card to the middle of the unused deck

**Returns:**
		
		Nothing
---
### shuffle:
Shuffles the unused cards in the deck

**Arguments:**
		
		None

**Returns:**	

		Nothing
---
### replace_used_cards:
Puts the used cards back into the bottom of the active deck.

**Arguments:**

        shuffle_used: (bool) Shuffles the used cards before putting the back into the deck. Calling this
                             will also clear the list of used cards. (DEFAULT = False)
		 shuffle: (bool) Shuffles the new deck which now includes the used and unused cards. (DEFAULT = False)

**Returns:**	

		Nothing
---
### dict_to_value:
Take a dictionary of face:int value. The unused deck is looped through and if the face key is found to
match the face of a card the value is updated for that card.

**Arguments:** 

        value_dict: (dict) Dictionary of key/values to update the int value of a card

**Returns:**

	 	Nothing
---
### get_deck_info:
Returns a dictionary containing the 'child_decks', 'suits', 'cards', 'wilds', 'special_cards' and
'total_cards' of the current deck.

**Arguments:**
		
		None

**Returns:**	

		dict
---
### clear_values:
Sets the integer value of all unused cards to 'None'

**Arguments:**
		
		None

**Returns:**	

		Nothing
---