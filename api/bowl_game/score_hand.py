#from dynamos.empty_discard import EmptyDiscard
#from dynamos.bottom_of_deck import BottomOfDeck
#from cards.deck import Deck

import cards
import dynamos

class ScoreHand:

    def __init__(self, hand):
        self.poker_hand = cards.PokerHand(hand)
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
        hands.append(cards.StraightFlush(self.poker_hand))
        hands.append(cards.FourOfAKind(self.poker_hand))
        hands.append(cards.FullHouse(self.poker_hand))
        hands.append(cards.Flush(self.poker_hand))
        hands.append(cards.Straight(self.poker_hand))
        hands.append(cards.ThreeOfAKind(self.poker_hand))
        hands.append(cards.TwoPairs(self.poker_hand))
        hands.append(cards.OnePair(self.poker_hand))
        hands.append(cards.HighCard(self.poker_hand))

        for hand in hands:
            if hand.is_match():
                return hand.get_rating()

