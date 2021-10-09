from dynamos.draw_cards import DrawCards as Draw
from dynamos.player_status import PlayerStatus
from helpers.sns_helpers import SnsHelpers

class DrawCards:

    @staticmethod
    def draw(game_id, player_id, number_of_cards):
        
        # get cards from deck
        (hand, deck_size) = Draw.execute(game_id, player_id, number_of_cards)

        #if stack <= 7:
        #    helpers.SnsHelpers.publish('')

        if number_of_cards in [3, 4] and len(hand) <= 5:
            player_status = 'finished'
        elif number_of_cards in [6] and len(hand) >= 5:
            player_status = 'mustdiscard+'
        elif number_of_cards not in [3, 4, 6] and hand_size >= 5:
            player_status = 'mustdiscard'
        else:
            player_status = 'dealt'

        # trigger scoring
        SnsHelpers.publish(
            TopicArn='',
            Message={
                'gameId': game_id,
                'playerId': player_id,
                'version': version,
                'hand': hand,
                'status': player_status
            },
            MessageAttributes={
                'MODE': {
                    'StringValue': 'SCORE_HAND'
                }
            }
        )

        return True

