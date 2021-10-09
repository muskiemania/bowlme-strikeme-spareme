#from dynamos.empty_discard import EmptyDiscard
#from dynamos.bottom_of_deck import BottomOfDeck
#from cards.deck import Deck

import cards
import dynamos

class ScoreHand:

    def __init__(self, hand):
        self.poker_hand = cards.poker_hand.PokerHand(hand)
        #print self.poker_hand

    @staticmethod
    def score(game_id, player_id, hand):
        # first score the hand
        scorer = ScoreHand(hand)
        rating = scorer.get_rating()
        
        # then write that data to dynamodb
        # then finished
        try:
            return dynamos.score_hand.ScoreHand.execute(game_id, player_id, str(rating))
        except:
            raise
    
    def get_rating(self):
        hands = []
        hands.append(cards.straight_flush.StraightFlush(self.poker_hand))
        hands.append(cards.four_of_a_kind.FourOfAKind(self.poker_hand))
        hands.append(cards.full_house.FullHouse(self.poker_hand))
        hands.append(cards.flush.Flush(self.poker_hand))
        hands.append(cards.straight.Straight(self.poker_hand))
        hands.append(cards.three_of_a_kind.ThreeOfAKind(self.poker_hand))
        hands.append(cards.two_pairs.TwoPairs(self.poker_hand))
        hands.append(cards.one_pair.OnePair(self.poker_hand))
        hands.append(cards.high_card.HighCard(self.poker_hand))

        for hand in hands:
            if hand.is_match():
                return hand.get_rating()

