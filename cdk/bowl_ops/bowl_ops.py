from aws_cdk import (
        Stack,
        aws_lambda as _lambda,
        aws_lambda_python_alpha as _python,
        aws_events as _events,
        aws_events_targets as targets
        )
from constructs import Construct
import json

class BowlOpsStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
       
        _games_table = kwargs.pop('games_table')
        _players_table = kwargs.pop('players_table')
        _event_bus = kwargs.pop('event_bus')
        #_bowl_events_rules = kwargs.pop('bowl_events_rules')

        super().__init__(scope, construct_id, **kwargs)

        # LAMBDA
        create_deck_lambda = _python.PythonFunction(
                self,
                'CreateDeck',
                entry='lambda',
                runtime=_lambda.Runtime.PYTHON_3_8,
                index='create_deck.py',
                handler='handler',
                environment={
                    'DYNAMODB': json.dumps({
                        'games_table': {
                            'table_name': _games_table.table_name}})})

        shuffle_deck_lambda = _python.PythonFunction(
                self,
                'ShuffleDeck',
                entry='lambda',
                runtime=_lambda.Runtime.PYTHON_3_8,
                index='shuffle_deck.py',
                handler='handler',
                environment={
                    'DYNAMODB': json.dumps({
                        'games_table': {
                            'table_name': _games_table.table_name}})})

        score_hand_lambda = _python.PythonFunction(
                self,
                'ScoreHand',
                entry='lambda',
                runtime=_lambda.Runtime.PYTHON_3_8,
                index='score_hand.py',
                handler='handler',
                environment={
                    'DYNAMODB': json.dumps({
                        'players_table': {
                            'table_name': _players_table.table_name}})})


        # GRANTS
        _games_table.grant_read_write_data(create_deck_lambda)
        _games_table.grant_read_write_data(shuffle_deck_lambda)
        _players_table.grant_read_write_data(score_hand_lambda)

        # EVENT BRIDGE RULES
        _create_deck_rule = _events.Rule(
                self,
                'BowlCreateDeck',
                event_bus=_event_bus)

        _create_deck_rule.add_event_pattern(
                source=['bowlapi.create_game'])
        _create_deck_rule.add_target(
                targets.LambdaFunction(create_deck_lambda))

        _shuffle_deck_rule = _events.Rule(
                self,
                'BowlShuffleDeck',
                event_bus=_event_bus)

        _shuffle_deck_rule.add_event_pattern(
                source=['bowlapi.game_status.start'])
        _shuffle_deck_rule.add_target(
                targets.LambdaFunction(shuffle_deck_lambda))

        _score_hand_rule = _events.Rule(
                self,
                'BowlScoreHand',
                event_bus=_event_bus)

        _score_hand_rule.add_event_pattern(
                source=['bowlapi.draw_cards', 'bowlapi.discard_cards'])
        _score_hand_rule.add_target(
                targets.LambdaFunction(score_hand_lambda))

