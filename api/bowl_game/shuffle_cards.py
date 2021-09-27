from dynamos.empty_discard import EmptyDiscard
from dynamos.bottom_of_deck import BottomOfDeck
from cards.deck import Deck

class ShuffleCards:

    @staticmethod
    def shuffle(game_id):
        
        # get cards from discard pile
        cards = dynamos.EmptyDiscard.execute(game_id)

        # shuffle cards
        shuffled = Deck.shuffle_cards(cards)

        # append shuffled cards to deck pile
        return dynamos.BottomOfDeck.execute(game_id, cards)



