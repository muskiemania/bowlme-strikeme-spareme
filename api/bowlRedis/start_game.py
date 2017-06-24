import redis
from cards import Deck
import datetime
from entities import Game, GameStatus

class StartGame:

    
    def __init__(self, game_id):
        self.redis = redis.StrictRedis()
        self.game_id = game_id

    def execute(self, host_player_id):
        #first check to see if player id host and that status is CREATED
        pipe = self.redis.pipeline()
        pipe.hgetall('game-%s-info' % self.game_id)
        info = pipe.execute()[0]

        if 'host_id' not in info:
            raise Exception('no host available for this game')
        if not info['host_id'] == host_player_id:
            raise Exception('only the host can start a game')
        if 'status' not in info:
            raise Exception('status unknown - cannot start this game')
        if not info['status'] == str(GameStatus.CREATED.value):
            raise Exception('cannot start a game that is not in CREATED state')

        #now start the game:
        #shuffle up and deal
        #change game status

        game = Game(self.game_id, info['host_name'])
        game.status = GameStatus.STARTED
        game.last_updated = datetime.datetime.now()
        game.deck = Deck.generate_deck()
        game.deck.shuffle_deck()
        
        info = {}
        info['status'] = game.status.value
        pipe.hmset('game-%s-info' % self.game_id, info)
        pipe.rpush('game-%s-deck' % self.game_id, *Deck.show_cards(game.deck.get_deck()))

        updated = {}
        updated['%s-updated' % self.game_id] = game.last_updated
        updated['%s-status' % self.game_id] = game.status.value
        pipe.hmset('game-last-updated', updated)

        pipe.execute()
        return game
        
