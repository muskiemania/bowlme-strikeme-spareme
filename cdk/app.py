#!/usr/bin/env python3
import os

import aws_cdk as cdk

from core_infra.core_infra import CoreInfraStack
from bowl_api.bowl_api import BowlApiStack
from bowl_ops.bowl_ops import BowlOpsStack

app = cdk.App()

core = CoreInfraStack(app, 'BowlCoreInfraStack',
                env=cdk.Environment(
                    account=os.getenv('CDK_DEFAULT_ACCOUNT'), 
                    region=os.getenv('CDK_DEFAULT_REGION')))

api = BowlApiStack(app, 'BowlCoreApiStack',
                env=cdk.Environment(
                    account=os.getenv('CDK_DEFAULT_ACCOUNT'), 
                    region=os.getenv('CDK_DEFAULT_REGION')),
                event_bus=core.event_bus,
                games_table=core.games_table,
                players_table=core.players_table)

ops = BowlOpsStack(app, 'BowlCoreOpsStack',
                env=cdk.Environment(
                    account=os.getenv('CDK_DEFAULT_ACCOUNT'),
                    region=os.getenv('CDK_DEFAULT_REGION')),
                games_table=core.games_table,
                players_table=core.players_table,
                event_bus=core.event_bus)

app.synth()
