import dynamos
import uuid
from cards.deck import Deck

class CreateGame:

    @staticmethod
    def create(number_of_decks):
        
        # create a game_id
        _game_id = str(uuid.UUID4())

        # create cards
        _deck = Deck.generate(number_of_decks)
        _cards = _deck.cards()
        
        dynamos.CreateGame.create(_game_id, cards)

        return _game_id
