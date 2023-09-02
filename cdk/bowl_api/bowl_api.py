from aws_cdk import (
        Stack,
        aws_lambda as _lambda,
        aws_lambda_python_alpha as _python,
        aws_events as _events
        )
from constructs import Construct
import json

class BowlApiStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
       
        _games_table = kwargs.pop('games_table')
        _players_table = kwargs.pop('players_table')

        super().__init__(scope, construct_id, **kwargs)

        # LAMBDA-LAYER
        jwt_layer = _python.PythonLayerVersion(
                self,
                'JwtLayer',
                entry='layers/jwt_layer',
                compatible_runtimes=[_lambda.Runtime.PYTHON_3_8],
                description='PyJWTLibrary',
                layer_version_name='PyJWTLibrary')

        # LAMBDA
        create_game_lambda = _python.PythonFunction(
                self,
                'CreateGame',
                entry='lambda',
                runtime=_lambda.Runtime.PYTHON_3_8,
                layers=[jwt_layer],
                index='create_game.py',
                handler='handler',
                environment={
                    'DYNAMODB': json.dumps({
                        'games_table': {
                            'table_name': _games_table.table_name},
                        'players_table': {
                            'table_name': _players_table.table_name}})})

        _games_table.grant_read_write_data(create_game_lambda)
        _players_table.grant_read_write_data(create_game_lambda)
