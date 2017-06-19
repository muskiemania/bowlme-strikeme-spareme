import redis
import cards

class DrawCards:

    def __init__(self):
        self.r = redis.StrictRedis()
        self.game = None
        self.player = None
        self.hand = None
        self.deck = None

    def Init(self, gameId, handId):
        self.gameId = gameId
        self.handId = handId

    def Draw(numberOfCards = 1):
        while numberOfCards > 0:
            p = self.r.pipeline()
            p.rpoplpush('game-%s-deck' % self.gameId, 'game-%s-hand-%s' % (self.gameId, self.handId))
            p.execute()

            p.llen('game-%s-deck' % self.gameId)
            deckSize = p.execute()

            if deckSize == 1:
                self.__ShuffleDeck()

            numberOfCards = numberOfCards - 1

        return

    def __ShuffleDeck(self):
        p = self.r.pipeline()
        p.lrange('game-%s-discard' % self.gameId, 0, -1)
        disard = p.execute()
        shuffled = Deck.ShuffleCards(map(lambda x: Card(x), discard))
        for card in shuffled:
            p.lpush('game-%s-deck' % self.gameId, card)
        p.ltrim('game-%s-discard' % self.gameId, -1, 0)
        p.execute()
        
