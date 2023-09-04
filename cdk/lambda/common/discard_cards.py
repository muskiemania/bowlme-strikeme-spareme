import boto3
import json
import os

class DiscardCards:

    @staticmethod
    def discard(**kwargs):

        _game_id = kwargs.get('game_id')
        _player_id = kwargs.get('player_id')
        _cards = kwargs.get('cards')

        _table_metadata = json.loads(os.environ['DYNAMODB'])
        _games_table_name = _table_metadata.get('games_table').get('table_name')
        _players_table_name = _table_metadata.get('players_table').get('table_name')

        # then get the players hand
        _dynamo = boto3.client('dynamodb')
        reply = _dynamo.get_item(
                TableName=_players_table_name,
                Key={
                    'Game_Id': {
                        'S': _game_id},
                    'Player_Id': {
                        'S': _player_id}},
                ConsistentRead=True,
                ProjectionExpression='#hand',
                ExpressionAttributeNames={
                    '#hand': 'Hand'})


        # must remove cards from player hand
        hand = reply['Item']['Hand']['L']
        cards = [c['S'] for c in hand]

        _to_discard = []

        for each in _cards:
            try:
                cards.remove(each)
                _to_discard.append(each)
            except ValueError as e:
                continue

        # put new hand back to player
        reply = _dynamo.update_item(
                TableName=_players_table_name,
                Key={
                    'Game_Id': {
                        'S': _game_id},
                    'Player_Id': {
                        'S': _player_id}},
                UpdateExpression='SET #hand = :cards',
                ExpressionAttributeNames={
                    '#hand': 'Hand'},
                ExpressionAttributeValues={
                    ':cards': {'L': [{'S': card} for card in cards]}})

        # appended discarded to discard pile
        reply = _dynamo.update_item(
                TableName=_games_table_name,
                Key={
                    'Game_Id': {
                        'S': _game_id}},
                    UpdateExpression='SET #discard = list_append(#discard, :discards)',
                ExpressionAttributeNames={
                    '#discard': 'Discard'},
                ExpressionAttributeValues={
                    ':discards': {'L': [{'S': card} for card in _to_discard]}})

        _event_metadata = json.loads(os.environ['EVENTBRIDGE'])
        _event_bus_name = _event_metadata.get('event_bus').get('event_bus_name')
        _events = boto3.client('events')
 
        # need to score player hand
        _events.put_events(
                Entries=[
                    {
                        'Detail': json.dumps({
                            'Action': 'score_hand',
                            'Game_Id': _game_id,
                            'Player_Id': _player_id}),
                        'DetailType': 'score a hand',
                        'Source': 'bowlapi.discard_cards',
                        'EventBusName': _event_bus_name}])

        return
