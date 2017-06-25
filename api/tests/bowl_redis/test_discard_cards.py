from entities import GameStatus, PlayerStatus
import bowl_redis
import redis

class Test_RedisDiscardCards:

    def test_draw_cards_constructor(self):
        game_id = 100
        player_id = 'asdfqwerty'
        draw_cards = bowl_redis.DrawCards(game_id, player_id)

        assert draw_cards.game_id == game_id
        assert draw_cards.player_id == player_id

    def setup_game(self):
        create_game = bowl_redis.CreateGame('Justin')
        game = create_game.execute()

        start_game = bowl_redis.StartGame(game.game_id)
        host_player_id = game.players[0].player_id
        start_game.execute(host_player_id)

        return (game.game_id, host_player_id)

    def setup_deck_discard_and_hand(self, key_info, deck, discard, hand):
        r = redis.StrictRedis()
        pipe = r.pipeline()

        pipe.delete(key_info.game_deck())
        pipe.rpush(key_info.game_deck(), *deck)
        pipe.delete(key_info.game_discard())
        pipe.rpush(key_info.game_discard(), *discard)
        pipe.delete(key_info.game_player_hand())
        pipe.rpush(key_info.game_player_hand(), *hand)
        pipe.execute()

        return

    def test_discard_cards_execute_discard_one_card(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        r.flushall()
        pipe.execute()

        (game_id, host_player_id) = self.setup_game()
        key_info = bowl_redis.RedisKeys(game_id, host_player_id)

        test_deck = ['AS', 'KS', '3S', '5S']
        test_discard = ['7C', '3C', '2C']
        test_hand = ['7H', '8H', '2H', 'TH', 'JH', '9H']
        self.setup_deck_discard_and_hand(key_info, test_deck, test_discard, test_hand)

        discard_cards = bowl_redis.DiscardCards(game_id, host_player_id)
        discard_cards.execute(['2H'])

        pipe.lrange(key_info.game_deck(), 0, -1)
        pipe.lrange(key_info.game_discard(), 0, -1)
        pipe.lrange(key_info.game_player_hand(), 0, -1)

        [deck, discard, hand] = pipe.execute()

        test_discard.append('2H')
        
        assert deck == test_deck
        assert discard == test_discard
        assert set(hand) == set(['JH', '7H', '8H', 'TH', '9H'])

    def test_discard_cards_execute_discard_two_cards(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        r.flushall()
        pipe.execute()

        (game_id, host_player_id) = self.setup_game()
        key_info = bowl_redis.RedisKeys(game_id, host_player_id)

        test_deck = ['AS', 'KS', '3S', '5S']
        test_discard = ['7C', '3C', '2C']
        test_hand = ['7H', '8H', '2H', 'TH', 'JH', '9H', 'AH']
        self.setup_deck_discard_and_hand(key_info, test_deck, test_discard, test_hand)

        discard_cards = bowl_redis.DiscardCards(game_id, host_player_id)
        discard_cards.execute(['2H', 'AH'])

        pipe.lrange(key_info.game_deck(), 0, -1)
        pipe.lrange(key_info.game_discard(), 0, -1)
        pipe.lrange(key_info.game_player_hand(), 0, -1)

        [deck, discard, hand] = pipe.execute()

        test_discard.append('2H')
        test_discard.append('AH')
        
        assert deck == test_deck
        assert discard == test_discard
        assert set(hand) == set(['JH', '7H', '8H', 'TH', '9H'])

    def test_discard_cards_execute_discard_one_card_fail(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        r.flushall()
        pipe.execute()

        (game_id, host_player_id) = self.setup_game()
        key_info = bowl_redis.RedisKeys(game_id, host_player_id)

        test_deck = ['AS', 'KS', '3S', '5S']
        test_discard = ['7C', '3C', '2C']
        test_hand = ['7H', '8H', '2H', 'TH', 'JH', '9H']
        self.setup_deck_discard_and_hand(key_info, test_deck, test_discard, test_hand)

        discard_cards = bowl_redis.DiscardCards(game_id, host_player_id)
        discard_cards.execute(['3H'])

        pipe.lrange(key_info.game_deck(), 0, -1)
        pipe.lrange(key_info.game_discard(), 0, -1)
        pipe.lrange(key_info.game_player_hand(), 0, -1)

        [deck, discard, hand] = pipe.execute()

        assert deck == test_deck
        assert discard == test_discard
        assert set(hand) == set(['JH', '7H', '8H', 'TH', '9H', '2H'])

    def test_draw_cards_execute_discard_two_cards_one_fail(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        r.flushall()
        pipe.execute()

        (game_id, host_player_id) = self.setup_game()
        key_info = bowl_redis.RedisKeys(game_id, host_player_id)

        test_deck = ['AS', 'KS', '3S', '5S']
        test_discard = ['7C', '3C', '2C']
        test_hand = ['7H', '8H', '2H', 'TH', 'JH', '9H', '3H']
        self.setup_deck_discard_and_hand(key_info, test_deck, test_discard, test_hand)

        discard_cards = bowl_redis.DiscardCards(game_id, host_player_id)
        discard_cards.execute(['2H', '4H'])

        pipe.lrange(key_info.game_deck(), 0, -1)
        pipe.lrange(key_info.game_discard(), 0, -1)
        pipe.lrange(key_info.game_player_hand(), 0, -1)

        [deck, discard, hand] = pipe.execute()

        test_discard.append('2H')
        
        assert deck == test_deck
        assert discard == test_discard
        assert set(hand) == set(['JH', '7H', '8H', 'TH', '9H', '3H'])
