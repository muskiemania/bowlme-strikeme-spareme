from aws_cdk import (
    # Duration,
    Stack,
    aws_dynamodb as dynamo,
    aws_lambda as lambda_,
    aws_lambda_python_alpha as python_
    # aws_sqs as sqs,
)
from constructs import Construct
import json

class PocStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # s3 bucket for generated images

        # DYNAMODB
        # dynamodb table for bowling data
        training_table = dynamo.Table(self,
            'bowling-training-table',
            partition_key=dynamo.Attribute(
                name='series_id',
                type=dynamo.AttributeType.STRING
            ),
            sort_key=dynamo.Attribute(
                name='game_number',
                type=dynamo.AttributeType.NUMBER
            )
        )


        # LAMBDA
        create_throw = python_.PythonFunction(self,
            'create_throw_lambda',
            entry='lambda_/create_throw',
            index='package/function.py',
            handler='handler',
            runtime=lambda_.Runtime.PYTHON_3_12,
            environment={
                'DYNAMODB': json.dumps({
                    'bowling-training-table': {
                        'table_name': training_table.table_name
                    }
                })
            }
        )

        # lambda to write to dynamodb
        # lambda to handle stream event, create analysis image
        # lambda to handle stream event, re-score
        # lambda to handle object created (analysis image)
        # lambda to create presigned url, trigger step fn
        
        # GRANTS
        training_table.grant_read_write_data(create_throw)



        # example resource
        # queue = sqs.Queue(
        #     self, "PocQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
