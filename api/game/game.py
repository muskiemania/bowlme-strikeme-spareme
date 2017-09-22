import bowl_redis
import entities
import cards
import scoring

class Game(object):

    def __init__(self):
        pass

    @staticmethod
    def get(game_id, player_id):
        game = bowl_redis.GetGame(game_id).get()

        response = entities.APIGameResponse()
        response.game_id = game_id

        game_status = entities.APIGameStatus()
        game_status.game_status_id = game.game_status
        game_status.game_status_text = entities.GameStatus.text(game.game_status)

        response.game_status = game_status

        response.last_updated = entities.APILastUpdated(game.last_updated)

        if player_id == game.host_player_id:
            response.is_host = True

        api_players = []
        for player in bowl_redis.GetPlayers(game_id).get():
            api_player = entities.APIPlayer(player.player_id, player.player_name)
            player_status = entities.APIPlayerStatus()
            player_status.player_status_id = player.player_status
            player_status.player_status_text = entities.PlayerStatus.text(player.player_status)
            api_player.player_status = player_status

            scorer = scoring.Scorer(player.hand)
            
            api_player.hand_rating = entities.APIHandRating(scorer.get_rating(), show_cards=game.game_status==entities.GameStatus.FINISHED)
                            
            api_players.append(api_player)

            if player.player_id == player_id:
                response.cards = [entities.APICard(card) for card in player.hand.cards]

        response.players = api_players

        
        
        return response
