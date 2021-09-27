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

        # append shuffled cards to deck pile
        return BottomOfDeck.execute(game_id, cards)



