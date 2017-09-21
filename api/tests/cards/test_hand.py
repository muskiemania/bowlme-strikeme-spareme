from cards import Card,Deck,Hand
import pytest

class Test_Hand():

    def __get_cards(self, cards=[]):
        return map(lambda x: Card(x), cards)
    
    def test_constuctor_cards_none(self):
        hand = Hand()
        assert len(hand.cards) == 0

    def test_constructor_cards(self):
        my_cards = ['AS','5C']
        hand = Hand(self.__get_cards(my_cards))
        
        assert my_cards == hand.show_cards()

    def _draw_cards_none(self):
        my_cards = ['KH']
        hand = Hand(self.__get_cards(my_cards))
        hand.draw_cards()
        assert my_cards == hand.show_cards()

    def _draw_cards_one(self):
        my_cards = ['TS']
        hand = Hand(self.__get_cards(my_cards))
        hand.draw_cards(self.__get_cards(['TC']))

        assert ['TS','TC'] == hand.show_cards()

    def _draw_cards_some(self):
        my_cards = ['4D','6D','8H']
        hand = Hand(self.__get_cards(my_cards))
        hand.draw_cards(self.__get_cards(['5C','7H']))

        assert ['4D','6D','8H','5C','7H'] == hand.show_cards()

    def _discard_none(self):
        my_cards = ['2S','3C','4D','5H','6S']
        hand = Hand(self.__get_cards(my_cards))
        hand.discard()

        assert my_cards == hand.show_cards()

    def _discard_one(self):
        my_cards = ['2S','QS','3C','4D','5H']
        hand = Hand(self.__get_cards(my_cards))
        hand.discard(self.__get_cards(['QS']))

        del my_cards[1]
        assert my_cards == hand.show_cards()

    def _discard_two(self):
        my_cards = ['2S','QS','TC','4D','5H']
        hand = Hand(self.__get_cards(my_cards))
        hand.discard(self.__get_cards(['TC','QS']))

        del my_cards[2]
        del my_cards[1]
        assert my_cards == hand.show_cards()

    def _discard_invalid(self):
        hand = Hand()
        with pytest.raises(Exception) as e:
            hand.discard(self.__get_cards(['AS']))
