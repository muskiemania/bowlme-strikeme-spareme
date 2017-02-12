from cards import Card,Deck,Hand
import pytest

class Test_Hand():

    def __getCards(self, cards=[]):
        return map(lambda x: Card(x), cards)
    
    def test_constuctor_cards_none(self):
        hand = Hand()
        assert len(hand.cards) == 0

    def test_constructor_cards(self):
        myCards = ['AS','5C']
        hand = Hand(self.__getCards(myCards))
        
        assert myCards == hand.ShowCards()

    def test_draw_cards_none(self):
        myCards = ['KH']
        hand = Hand(self.__getCards(myCards))
        hand.DrawCards()
        assert myCards == hand.ShowCards()

    def test_draw_cards_one(self):
        myCards = ['TS']
        hand = Hand(self.__getCards(myCards))
        hand.DrawCards(self.__getCards(['TC']))

        assert ['TS','TC'] == hand.ShowCards()

    def test_draw_cards_some(self):
        myCards = ['4D','6D','8H']
        hand = Hand(self.__getCards(myCards))
        hand.DrawCards(self.__getCards(['5C','7H']))

        assert ['4D','6D','8H','5C','7H'] == hand.ShowCards()

    def test_discard_none(self):
        myCards = ['2S','3C','4D','5H','6S']
        hand = Hand(self.__getCards(myCards))
        hand.Discard()

        assert myCards == hand.ShowCards()

    def test_discard_one(self):
        myCards = ['2S','QS','3C','4D','5H']
        hand = Hand(self.__getCards(myCards))
        hand.Discard(self.__getCards(['QS']))

        del myCards[1]
        assert myCards == hand.ShowCards()

    def test_discard_two(self):
        myCards = ['2S','QS','TC','4D','5H']
        hand = Hand(self.__getCards(myCards))
        hand.Discard(self.__getCards(['TC','QS']))

        del myCards[2]
        del myCards[1]
        assert myCards == hand.ShowCards()

    def test_discard_invalid(self):
        hand = Hand()
        with pytest.raises(Exception) as e:
            hand.Discard(self.__getCards(['AS']))
        
