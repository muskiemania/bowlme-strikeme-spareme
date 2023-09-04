import boto3
import json
import os

class DrawCards:

    @staticmethod
    def draw(**kwargs):

        _game_id = kwargs.get('game_id')
        _player_id = kwargs.get('player_id')
        _cards = kwargs.get('cards')

        _table_metadata = json.loads(os.environ['DYNAMODB'])
        _games_table_name = _table_metadata.get('games_table').get('table_name')
        _players_table_name = _table_metadata.get('players_table').get('table_name')

        # first lock the games table
        _dynamo = boto3.client('dynamodb')
        reply = _dynamo.update_item(
                TableName=_games_table_name,
                Key={
                    'Game_Id': {
                        'S': _game_id}},
                UpdateExpression='SET #lock = :drawing',
                ConditionExpression='#lock = :unlocked',
                ExpressionAttributeNames={
                    '#lock': 'Lock'},
                ExpressionAttributeValues={
                    ':drawing': {'S': 'drawing'},
                    ':unlocked': {'S': 'unlocked'}})

        # then get the deck
        reply = _dynamo.get_item(
                TableName=_games_table_name,
                Key={
                    'Game_Id': {
                        'S': _game_id}},
                ConsistentRead=True,
                ProjectionExpression='#deck',
                ExpressionAttributeNames={
                    '#deck': 'Deck'})


        # take n cards from deck
        # will add n cards to player hand
        deck = reply['Item']['Deck']['L']
        cards = [c['S'] for c in deck]

        to_player = cards[:_cards]
        to_deck = cards[_cards:]

        # add n cards to player hand
        reply = _dynamo.update_item(
                TableName=_players_table_name,
                Key={
                    'Game_Id': {
                        'S': _game_id},
                    'Player_Id': {
                        'S': _player_id}},
                UpdateExpression='SET #hand = list_append(#hand, :cards)',
                ExpressionAttributeNames={
                    '#hand': 'Hand'},
                ExpressionAttributeValues={
                    ':cards': {'L': [{'S': card} for card in to_player]}})

        # reset deck, unlock
        reply = _dynamo.update_item(
                TableName=_games_table_name,
                Key={
                    'Game_Id': {
                        'S': _game_id}},
                UpdateExpression='SET #deck = :deck, #lock = :unlocked',
                ConditionExpression='#lock = :drawing',
                ExpressionAttributeNames={
                    '#deck': 'Deck',
                    '#lock': 'Lock'},
                ExpressionAttributeValues={
                    ':deck': {'L': [{'S': card} for card in to_deck]},
                    ':drawing': {'S': 'drawing'},
                    ':unlocked': {'S': 'unlocked'}})

        _event_metadata = json.loads(os.environ['EVENTBRIDGE'])
        _event_bus_name = _event_metadata.get('event_bus').get('event_bus_name')
        _events = boto3.client('events')
 
        if len(to_deck) < 5:
            # need to shuffle
            _events.put_events(
                Entries=[
                    {
                        'Detail': json.dumps({
                            'Action': 'draw_cards',
                            'Game_Id': _game_id}),
                        'DetailType': 'draw cards from deck',
                        'Source': 'bowlapi.draw_cards',
                        'EventBusName': _event_bus_name}])

        # need to score player hand
        _events.put_events(
                Entries=[
                    {
                        'Detail': json.dumps({
                            'Action': 'score_hand',
                            'Game_Id': _game_id,
                            'Player_Id': _player_id}),
                        'DetailType': 'score a hand',
                        'Source': 'bowlapi.draw_cards',
                        'EventBusName': _event_bus_name}])

        return
