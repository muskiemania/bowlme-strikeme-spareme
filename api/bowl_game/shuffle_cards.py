from dynamos.empty_discard import EmptyDiscard
from dynamos.bottom_of_deck import BottomOfDeck
from cards.deck import Deck

class ShuffleCards:

    @staticmethod
    def shuffle(game_id):
        
        # get cards from discard pile
        cards = EmptyDiscard.execute(game_id)

        # shuffle cards
        shuffled = Deck.shuffle_cards(cards)
        shuffled = Deck.shuffle_cards(shuffled)
        shuffled.reverse()
        shuffled = Deck.shuffle_cards(shuffled)
        shuffled = Deck.shuffle_cards(shuffled)
        shuffled.reverse()
        shuffled = Deck.shuffle_cards(shuffled)
        shuffled = Deck.shuffle_cards(shuffled)

        # append shuffled cards to deck pile
        return BottomOfDeck.execute(game_id, shuffled)



