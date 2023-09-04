from aws_cdk import (
        Stack,
        aws_lambda as _lambda,
        aws_lambda_python_alpha as _python
        )
from constructs import Construct
import json

class BowlApiStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:

        _event_bus = kwargs.pop('event_bus')
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
                            'table_name': _players_table.table_name}}),
                    'EVENTBRIDGE': json.dumps({
                        'event_bus': {
                            'event_bus_name': _event_bus.event_bus_name}})})

        join_game_lambda = _python.PythonFunction(
                self,
                'JoinGame',
                entry='lambda',
                runtime=_lambda.Runtime.PYTHON_3_8,
                layers=[jwt_layer],
                index='join_game.py',
                handler='handler',
                environment={
                    'DYNAMODB': json.dumps({
                        'games_table': {
                            'table_name': _games_table.table_name},
                        'players_table': {
                            'table_name': _players_table.table_name}})})

        game_status_lambda = _python.PythonFunction(
                self,
                'GameStatus',
                entry='lambda',
                runtime=_lambda.Runtime.PYTHON_3_8,
                layers=[jwt_layer],
                index='change_status.py',
                handler='handler',
                environment={
                    'EVENTBRIDGE': json.dumps({
                        'event_bus': {
                            'event_bus_name': _event_bus.event_bus_name}})})

        draw_cards_lambda = _python.PythonFunction(
                self,
                'DrawCards',
                entry='lambda',
                runtime=_lambda.Runtime.PYTHON_3_8,
                index='draw_cards.py',
                handler='handler',
                environment={
                    'DYNAMODB': json.dumps({
                        'games_table': {
                            'table_name': _games_table.table_name},
                        'players_table': {
                            'table_name': _players_table.table_name}}),
                    'EVENTBRIDGE': json.dumps({
                        'event_bus': {
                            'event_bus_name': _event_bus.event_bus_name}})})

        discard_cards_lambda = _python.PythonFunction(
                self,
                'DiscardCards',
                entry='lambda',
                runtime=_lambda.Runtime.PYTHON_3_8,
                index='discard_cards.py',
                handler='handler',
                environment={
                    'DYNAMODB': json.dumps({
                        'games_table': {
                            'table_name': _games_table.table_name},
                        'players_table': {
                            'table_name': _players_table.table_name}}),
                    'EVENTBRIDGE': json.dumps({
                        'event_bus': {
                            'event_bus_name': _event_bus.event_bus_name}})})


        # GRANTS
        _games_table.grant_read_write_data(create_game_lambda)
        _games_table.grant_read_data(join_game_lambda)
        _games_table.grant_read_write_data(draw_cards_lambda)
        _games_table.grant_read_write_data(discard_cards_lambda)
 
        _players_table.grant_read_write_data(create_game_lambda)
        _players_table.grant_read_write_data(join_game_lambda)
        _players_table.grant_read_write_data(draw_cards_lambda)
        _players_table.grant_read_write_data(discard_cards_lambda)

        _event_bus.grant_put_events_to(create_game_lambda)
        _event_bus.grant_put_events_to(game_status_lambda)
        _event_bus.grant_put_events_to(draw_cards_lambda)
        _event_bus.grant_put_events_to(discard_cards_lambda)
