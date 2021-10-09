import json
from dynamos.draw_cards import DrawCards as Draw
from dynamos.player_status import PlayerStatus
from helpers.sns_helpers import SnsHelpers
from configs.sns import SnsConfigs
from configs.player_status import PlayerStatusConfigs

class DrawCards:

    @staticmethod
    def draw(game_id, player_id, number_of_cards):
        
        # get cards from deck
        (hand, version, deck_size) = Draw.execute(game_id, player_id, number_of_cards)

        #if stack <= 7:
        #    helpers.SnsHelpers.publish('')

        if number_of_cards in [3, 4] and len(hand) <= 5:
            player_status = PlayerStatusConfigs.FINISHED.value
        elif number_of_cards in [6] and len(hand) >= 5:
            player_status = PlayerStatusConfigs.FINISHED_MUST_DISCARD.value
        elif number_of_cards not in [3, 4, 6] and len(hand) >= 5:
            player_status = PlayerStatusConfigs.MUST_DISCARD.value
        else:
            player_status = PlayerStatusConfigs.DEALT.value

        # trigger scoring
        SnsHelpers.publish(
            TopicArn=SnsConfigs.SCORING_TOPIC_ARN.value,
            Message={
                'gameId': game_id,
                'playerId': player_id,
                'version': str(version),
                'hand': hand,
                'status': player_status
            },
            MessageAttributes={
                'MODE': {
                    'DataType': 'String',
                    'StringValue': 'SCORE_HAND'
                }
            }
        )

        return True

