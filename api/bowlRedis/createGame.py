import redis
import cards

class CreateGame:

    
    def __init__(self):
        self.r = redis.StrictRedis()
        self.game_id = None
        self.host = None
        self.players = None
        self.deck = None
        self.discard = None
        self.status = None

    def init(self, create_game):
        self.game_id = create_game.game_id
        self.host = create_game.host
        self.players = create_game.players
        self.deck =  cards.Deck.show_cards(create_game.deck.cards)
        self.discard = create_game.discard
        self.status = create_game.status

    def execute(self):

        #need a list for the deck - game-id-deck
        #need a list for the discard - game-id-discard
        #need a list for each players hand game-id-player-hand
        #need a hash for game info: host, status game-id-info:
        #hash for each players name - game-id-name:playerid
        #hash for each players hand - game-id-status:playerid
        p = self.r.pipeline()

        p.delete('game-%s-deck' % self.game_id)
        p.rpush('game-%s-deck' % self.game_id, *list(self.deck))
        p.hmset('game-%s-info' % self.game_id, {'host': self.host, 'status': self.status})
        p.hmset('game-%s-name' % self.game_id, {'%s' % self.host: self.players[self.host]['player_name']})
        p.hmset('game-%s-status' % self.game_id, {'%s' % self.host: 0})
        p.execute()

        return True

    def get(self, key, field=None):
        suffix = key.split('-')[2]
        if suffix == 'deck':
            return self.r.lrange(key, 0, -1)
        elif suffix == 'info' or suffix == 'name' or suffix == 'status':
            return self.r.hget(key, field)
