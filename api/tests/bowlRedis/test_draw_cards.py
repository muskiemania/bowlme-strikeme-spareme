from entities import GameStatus, PlayerStatus
import bowlRedis
import redis

class Test_RedisDrawCards:

    def test_draw_cards_constructor(self):
        game_id = 100
        player_id = 'asdfqwerty'
        draw_cards = bowlRedis.DrawCards(game_id, player_id)

        assert draw_cards.game_id == game_id
        assert draw_cards.player_id == player_id

    def setup_game(self):
        create_game = bowlRedis.CreateGame('Justin')
        game = create_game.execute()

        start_game = bowlRedis.StartGame(game.game_id)
        host_player_id = game.players[0].player_id
        start_game.execute(host_player_id)

        return (game.game_id, host_player_id)

    def setup_deck_and_discard(self, key_info, deck, discard):
        r = redis.StrictRedis()
        pipe = r.pipeline()

        pipe.delete(key_info.game_deck())
        pipe.rpush(key_info.game_deck(), *deck)
        pipe.delete(key_info.game_discard())
        pipe.rpush(key_info.game_discard(), *discard)
        pipe.execute()

        return

    def test_draw_cards_execute_empty_hand_draw_one_card_no_shuffle(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        r.flushall()
        pipe.execute()

        (game_id, host_player_id) = self.setup_game()
        key_info = bowlRedis.RedisKeys(game_id, host_player_id)

        test_deck = ['AS', 'KS', '3S', '5S']
        test_discard = ['7C', '3C', '2C']
        self.setup_deck_and_discard(key_info, test_deck, test_discard)

        draw_cards = bowlRedis.DrawCards(game_id, host_player_id)
        draw_cards.execute()

        pipe.lrange(key_info.game_deck(), 0, -1)
        pipe.lrange(key_info.game_discard(), 0, -1)
        pipe.lrange(key_info.game_player_hand(), 0, -1)

        [deck, discard, hand] = pipe.execute()

        assert deck == test_deck[0:-1]
        assert discard == test_discard
        assert set(hand) == set(['5S'])

    def test_draw_cards_execute_empty_hand_draw_two_cards_no_shuffle(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        r.flushall()
        pipe.execute()

        (game_id, host_player_id) = self.setup_game()
        key_info = bowlRedis.RedisKeys(game_id, host_player_id)

        test_deck = ['AS', 'KS', '3S', '5S']
        test_discard = ['7C', '3C', '2C']
        self.setup_deck_and_discard(key_info, test_deck, test_discard)

        draw_cards = bowlRedis.DrawCards(game_id, host_player_id)
        draw_cards.execute(2)

        pipe.lrange(key_info.game_deck(), 0, -1)
        pipe.lrange(key_info.game_discard(), 0, -1)
        pipe.lrange(key_info.game_player_hand(), 0, -1)

        [deck, discard, hand] = pipe.execute()

        assert deck == test_deck[0:-2]
        assert discard == test_discard
        assert set(hand) == set(['5S', '3S'])
        assert set(hand) == set(['3S', '5S'])

    def test_draw_cards_execute_empty_hand_draw_one_card_with_shuffle(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        r.flushall()
        pipe.execute()

        (game_id, host_player_id) = self.setup_game()
        key_info = bowlRedis.RedisKeys(game_id, host_player_id)

        test_deck = ['3S', '5S']
        test_discard = ['7C', '3C', '2C']
        self.setup_deck_and_discard(key_info, test_deck, test_discard)

        draw_cards = bowlRedis.DrawCards(game_id, host_player_id)
        draw_cards.execute()

        pipe.lrange(key_info.game_deck(), 0, -1)
        pipe.lrange(key_info.game_discard(), 0, -1)
        pipe.lrange(key_info.game_player_hand(), 0, -1)

        [deck, discard, hand] = pipe.execute()

        print deck
        print discard
        print hand
        assert deck[-1] == test_deck[-2]
        assert len(discard) == 0
        assert set(deck) == set(['3S', '7C', '3C', '2C'])
        assert set(hand) == set(['5S'])
        assert deck[0:-2] != test_discard
