from cards import PokerHand


class HighCard(PokerHand):

    def __init__(self):
        self.__rating = 1

    def is_match(self, hand):
        return True

    def get_rating(self, hand):
        tally = PokerHand.card_tally(hand)
        cards = sorted(tally.keys(), reverse=True) or []
        cards.extend([0, 0, 0, 0, 0])
        c = PokerHand.coalesce
        return (self.__rating, c(cards, 0, 0), c(cards, 1, 0), c(cards, 2, 0), c(cards, 3, 0), c(cards, 4, 0))
