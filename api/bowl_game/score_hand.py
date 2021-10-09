import cards.card
import cards.poker_hand
import cards.hand
import cards.straight_flush as sf
import cards.four_of_a_kind as fk
import cards.full_house as fh
import cards.flush as fl
import cards.straight as st
import cards.three_of_a_kind as tk
import cards.two_pairs as tp
import cards.one_pair as op
import cards.high_card as hc
import dynamos.score_hand

class ScoreHand:

    def __init__(self, hand):
        _hand = cards.hand.Hand([cards.card.Card(c) for c in hand])
        self.poker_hand = cards.poker_hand.PokerHand(_hand)

    @staticmethod
    def score(game_id, player_id, hand, version, status):
        # first score the hand
        scorer = ScoreHand(hand)
        rating = scorer.get_rating()
        
        # then write that data to dynamodb
        # then finished
        try:
            return dynamos.score_hand.ScoreHand.execute(game_id, player_id, str(rating), version, status)
        except:
            raise
    
    def get_rating(self):
        hands = []
        hands.append(sf.StraightFlush(self.poker_hand))
        hands.append(fk.FourOfAKind(self.poker_hand))
        hands.append(fh.FullHouse(self.poker_hand))
        hands.append(fl.Flush(self.poker_hand))
        hands.append(st.Straight(self.poker_hand))
        hands.append(tk.ThreeOfAKind(self.poker_hand))
        hands.append(tp.TwoPairs(self.poker_hand))
        hands.append(op.OnePair(self.poker_hand))
        hands.append(hc.HighCard(self.poker_hand))

        for hand in hands:
            if hand.is_match():
                return hand.get_rating()

