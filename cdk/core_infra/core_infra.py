from aws_cdk import (
        Stack,
        aws_dynamodb as dynamodb,
        aws_events as _events
        )
from constructs import Construct
import json

class CoreInfraStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # DYNAMODB
        self.games_table = dynamodb.Table(
                self, 
                'BowlGames',
                partition_key=dynamodb.Attribute(
                    name='Game_Id', 
                    type=dynamodb.AttributeType.STRING),
                billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
                time_to_live_attribute='TTL')

        self.players_table = dynamodb.Table(
                self,
                'BowlPlayers',
                partition_key=dynamodb.Attribute(
                    name='Game_Id',
                    type=dynamodb.AttributeType.STRING),
                sort_key=dynamodb.Attribute(
                    name='Player_Id',
                    type=dynamodb.AttributeType.STRING),
                billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
                time_to_live_attribute='TTL')

        self.players_table.add_global_secondary_index(
                partition_key=dynamodb.Attribute(
                    name='Connection_Id',
                    type=dynamodb.AttributeType.STRING),
                index_name='SocketConnectionIndex',
                projection_type=dynamodb.ProjectionType.KEYS_ONLY)

        # EVENTBRIDGE
        self.event_bus = _events.EventBus(
                self, 
                'BowlEvents',
                event_bus_name='BowlEvents')

