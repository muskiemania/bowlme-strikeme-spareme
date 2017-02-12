from cards import Hand, PokerHand

class Flush(PokerHand):

    def __init__(self):
        self.__rating = 6

    def IsMatch(self, hand):
        return len(PokerHand.getSuitTally(hand).keys()) == 1 and len(hand.cards) == 5

    def GetRating(self, hand):
        PokerHand.sortCards(hand)
        return (self.__rating, hand.cards[0].strength, hand.cards[1].strength, hand.cards[2].strength, hand.cards[3].strength, hand.cards[4].strength)
