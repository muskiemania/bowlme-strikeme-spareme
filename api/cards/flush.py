from cards import Hand, PokerHand

class Flush(PokerHand):

    def __init__(self):
        self.__rating = 6

    def is_match(self, hand):
        return len(PokerHand.get_suit_tally(hand).keys()) == 1 and len(hand.cards) == 5

    def get_rating(self, hand):
        PokerHand.sort_cards(hand)
        return (self.__rating, hand.cards[0].strength, hand.cards[1].strength, hand.cards[2].strength, hand.cards[3].strength, hand.cards[4].strength)
