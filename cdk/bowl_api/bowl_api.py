from aws_cdk import (
        Stack,
        aws_lambda as _lambda,
        aws_events as _events
        )
from constructs import Construct
import json

class BowlApiStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        
        _games_table = kwargs.pop('games_table')
        _players_table = kwargs.pop('players_table')

        super().__init__(scope, construct_id, **kwargs)

        # LAMBDA
        create_game_lambda = _lambda.Function(
                self,
                'CreateGame',
                runtime=_lambda.Runtime.PYTHON_3_8,
                code=_lambda.Code.from_asset('lambda'),
                handler='create_game.handler',
                environment={
                    'DYNAMODB': json.dumps({
                        'games_table': {
                            'table_name': _games_table.table_name},
                        'players_table': {
                            'table_name': _players_table.table_name}})})

        _games_table.grant_read_write_data(create_game_lambda)
        _players_table.grant_read_write_data(create_game_lambda)
