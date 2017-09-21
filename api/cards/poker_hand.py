from cards import Hand

class PokerHand(object):

    def __init__(self, hand=None):
        self.hand = hand
        #Hand.__init__(self, hand.cards or [])

    def sort_cards(self):
        self.hand.cards.sort(key=lambda x: x.strength, reverse=True)

    def card_tally(self):
        card_dictionary = {}
        for card in self.hand.cards:
            if card.strength not in card_dictionary.keys():
                card_dictionary[card.strength] = []
            card_dictionary[card.strength].append(card)

        return card_dictionary

    def get_suit_tally(self):
        suit_dictionary = {}
        for card in self.hand.cards:
            if card.suit not in suit_dictionary.keys():
                suit_dictionary[card.suit] = []
            suit_dictionary[card.suit].append(card)

        return suit_dictionary

    def coalesce(self, collection, index, default_value=0):
        return collection[index] if len(collection) > index else default_value
