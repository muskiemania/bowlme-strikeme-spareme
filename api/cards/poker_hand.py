class PokerHand(object):

    def __init__(self):
        pass

    @classmethod
    def sort_cards(cls, hand):
        hand.cards.sort(key=lambda x: x.strength, reverse=True)

    @classmethod
    def card_tally(cls, hand):
        card_dictionary = {}
        for card in hand.cards:
            if card.strength not in card_dictionary.keys():
                card_dictionary[card.strength] = []
            card_dictionary[card.strength].append(card)

        return card_dictionary

    @classmethod
    def get_suit_tally(cls, hand):
        suit_dictionary = {}
        for card in hand.cards:
            if card.suit not in suit_dictionary.keys():
                suit_dictionary[card.suit] = []
            suit_dictionary[card.suit].append(card)

        return suit_dictionary

    @classmethod
    def coalesce(cls, collection, index, default_value=0):
        return collection[index] if len(collection) > index else default_value
