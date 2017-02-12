from cards import Hand

class PokerHand():
    
    def __init__(self):
        pass

    @staticmethod
    def sortCards(hand):
        hand.cards.sort(key=lambda x: x.strength, reverse=True)

    @staticmethod
    def cardTally(hand):
        cardDict = {}
        for c in hand.cards:
            if c.strength not in cardDict.keys():
                cardDict[c.strength] = []
            cardDict[c.strength].append(c)

        return cardDict

    @staticmethod
    def getSuitTally(hand):
        suitDict = {}
        for c in hand.cards:
            if c.suit not in suitDict.keys():
                suitDict[c.suit] = []
            suitDict[c.suit].append(c)

        return suitDict

    @staticmethod
    def Coalesce(collection, index, defaultValue=0):
        print collection
        return collection[index] if len(collection) > index else defaultValue
