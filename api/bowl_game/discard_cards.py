import json
from dynamos.discard_cards import DiscardCards as Discard
from dynamos.player_status import PlayerStatus
from helpers.sns_helpers import SnsHelpers
from configs.sns import SnsConfigs
from configs.player_status import PlayerStatusConfigs

class DiscardCards:

    @staticmethod
    def discard(game_id, player_id, number_of_cards):
        
        # get cards from deck
        (hand, version, status) = Discard.execute(game_id, player_id, cards)

        if len(hand) > 5 and status in [PlayerStatusConfigs.FINISHED_MUST_DISCARD.value, PlayerStatusConfigs.MUST_DISCARD.value]:
            player_status = status
        elif len(hand) <= 5 and status in [PlayerStatusConfigs.FINISHED_MUST_DISCARD.value]:
            player_status = PlayerStatusConfigs.FINISHED.value
        elif len(hand) <=5 and status in [PlayerStatusConfigs.MUST_DISCARD.value]:
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

