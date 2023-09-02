#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk.cdk_stack import CdkStack

from core_infra.core_infra import CoreInfraStack
from bowl_api.bowl_api import BowlApiStack

app = cdk.App()

core = CoreInfraStack(app, 'BowlCoreInfraStack',
                env=cdk.Environment(
                    account=os.getenv('CDK_DEFAULT_ACCOUNT'), 
                    region=os.getenv('CDK_DEFAULT_REGION')))

BowlApiStack(app, 'BowlCoreApiStack',
                env=cdk.Environment(
                    account=os.getenv('CDK_DEFAULT_ACCOUNT'), 
                    region=os.getenv('CDK_DEFAULT_REGION')),
                games_table=core.games_table,
                players_table=core.players_table)

app.synth()
