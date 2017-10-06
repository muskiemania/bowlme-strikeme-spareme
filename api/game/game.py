import bowl_redis
import entities
import cards
import scoring
import viewmodels

class Game(object):

    def __init__(self):
        pass

    @staticmethod
    def get(game_id, player_id=None):

        players = bowl_redis.GetPlayers(game_id)
        player_dto = players.execute()

        print 'players'
        print map(lambda x: x.__dict__, player_dto)
        print '====='

        game_details = bowl_redis.GetGame(game_id)
        game_details_dto = game_details.execute()

        #needs:
        #all players, including name, hand, status
        #if player specified, then
        #  -- exclude "me" from players
        #  -- fetch my cards
        #  -- fetch my status
        #for the game
        #  -- need game status
        #  -- need to know if "I" am the host

        my_game = viewmodels.MyGameModel()

        if player_id is not None:
            players = filter(lambda x: x.player_id != player_id, player_dto)
            my_game.setPlayers(players)

            me = filter(lambda x: x.player_id == player_id, player_dto)
            print player_id
            print '###'
            print players
            print me
            
            if len(me) == 1:
                me = me[0]
                #my_game.setCards(me.cards)

                print '555'
                print me.__dict__
                print '555'
                my_game.setStatus(player_status=me.player_status)

            my_game.setStatus(game_status=game_details_dto.game_status)
            
        return my_game
