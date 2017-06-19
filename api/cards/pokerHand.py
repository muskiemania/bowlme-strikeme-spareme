from cards import Hand

class PokerHand():
    
    def __init__(self):
        pass

    @staticmethod
    def sort_cards(hand):
        hand.cards.sort(key=lambda x: x.strength, reverse=True)

    @staticmethod
    def card_tally(hand):
        card_dictionary = {}
        for card in hand.cards:
            if card.strength not in card_dictionary.keys():
                card_dictionary[card.strength] = []
            card_dictionary[card.strength].append(card)

        return card_dictionary

    @staticmethod
    def get_suit_tally(hand):
        suit_dictionary = {}
        for card in hand.cards:
            if card.suit not in suit_dictionary.keys():
                suit_dictionary[card.suit] = []
            suit_dictionary[card.suit].append(card)

        return suit_dictionary

    @staticmethod
    def coalesce(collection, index, default_value=0):
        print collection
        return collection[index] if len(collection) > index else default_value
