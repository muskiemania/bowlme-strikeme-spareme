from aws_cdk import (
    Duration,
    RemovalPolicy,
    Stack,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins,
    aws_dynamodb as dynamo,
    aws_lambda as lambda_,
    aws_lambda_python_alpha as python_,
    aws_s3 as s3,
    aws_apigatewayv2 as apigwv2,
    aws_apigatewayv2_integrations as apigwv2int
    # aws_sqs as sqs,
)
from constructs import Construct
import json

class PocStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # S3
        # s3 bucket for generated images
        bucket = s3.Bucket(self, 'bowl-analysis-bucket',
            encryption=s3.BucketEncryption.S3_MANAGED,
            versioned=False,
            removal_policy=RemovalPolicy.DESTROY
        )

        # CLOUDFRONT
        distribution = cloudfront.Distribution(self, 'bowl-analysis-distribution',
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3BucketOrigin.with_origin_access_control(bucket)
            )
        )

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

        # LAYERS
        #pillow_layer = lambda_.LayerVersion(
        #    self,
        #    'PillowLayer',
        #    code=lambda_.Code.from_asset('lambda_/layers/pillow/layer.zip'),
        #    compatible_runtimes=[lambda_.Runtime.PYTHON_3_12],
        #    layer_version_name='PillowLayer',
        #    description='Pillow')

        pillow_layer = lambda_.LayerVersion.from_layer_version_arn(
            self, 'PillowLayer', 'arn:aws:lambda:us-west-2:770693421928:layer:Klayers-p312-Pillow:5')

        matplotlib_layer = lambda_.LayerVersion(
            self,
            'MatplotlibLayer',
            code=lambda_.Code.from_asset('lambda_/layers/matplotlib/layer.zip'),
            compatible_runtimes=[lambda_.Runtime.PYTHON_3_12],
            layer_version_name='MatplotlibLayer',
            description='Matplotlib')

        matplotlib_numpy_layer = lambda_.LayerVersion(
            self,
            'MatplotlibNumpyLayer',
            code=lambda_.Code.from_asset('lambda_/layers/matplot_numpy/layer.zip'),
            compatible_runtimes=[lambda_.Runtime.PYTHON_3_12],
            layer_version_name='Matplotlib_Numpy_Layer',
            description='Matplotlib_Numpy')

        numpy_layer = lambda_.LayerVersion.from_layer_version_arn(
            self, 'NumpyLayer', 'arn:aws:lambda:us-west-2:770693421928:layer:Klayers-p312-numpy:11')

        scipy_layer = lambda_.LayerVersion.from_layer_version_arn(
            self, 'SciPyLayer', 'arn:aws:lambda:us-west-2:770693421928:layer:Klayers-p312-scipy:3')

        # LAMBDA
        create_throw = python_.PythonFunction(self,
            'create_throw_lambda',
            entry='lambda_/functions/create_throw',
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

        score_throws = python_.PythonFunction(self,
            'score_throws_lambda',
            entry='lambda_/functions/score_throws',
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

        curve_interpolate = python_.PythonFunction(self,
            'curve_interpolation_lambda',
            entry='lambda_/functions/curve_interpolate',
            index='package/function.py',
            handler='handler',
            layers=[scipy_layer],
            timeout=Duration.seconds(15),
            runtime=lambda_.Runtime.PYTHON_3_12,
        )

        generate_analysis = python_.PythonFunction(self,
            'generate_analysiis_lambda',
            entry='lambda_/functions/generate_analysis',
            index='package/function.py',
            handler='handler',
            layers=[pillow_layer],
            timeout=Duration.seconds(15),
            runtime=lambda_.Runtime.PYTHON_3_12,
            environment={
                'CLOUDFRONT': json.dumps({
                    'distribution': {
                        'domain_name': distribution.distribution_domain_name
                    }
                }),
                'DYNAMODB': json.dumps({
                    'bowling-training-table': {
                        'table_name': training_table.table_name
                    }
                }),
                'MPLCONFIGDIR': '/tmp/matplotlb',
                'S3': json.dumps({
                    'bowling-analysis-bucket': {
                        'bucket_name': bucket.bucket_name
                    }
                }),
                'LAMBDA': json.dumps({
                    'curve-interpolate-lambda': {
                        'function_name': curve_interpolate.function_name
                    }
                })
            }
        )

        get_series = python_.PythonFunction(self,
            'get_series_lambda',
            entry='lambda_/functions/get_series',
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

        # API GATEWAY

        http_api = apigwv2.HttpApi(self,
            'BowlingTrainerApi',
            description='Bowling Trainer API'
        )

        # INTEGRATIONS
        get_series_alias = lambda_.Alias(self,
            'GetSeriesAlias',
            alias_name=f'local-{get_series.current_version.version}',
            version=get_series.current_version
        )

        get_series_integration = apigwv2int.HttpLambdaIntegration(
            'GetSeriesIntegration',
            handler=get_series_alias
        )

        # ROUTES
        http_api.add_routes(
            path='/series/{series_id}',
            methods=[apigwv2.HttpMethod.GET, apigwv2.HttpMethod.OPTIONS],
            integration=get_series_integration
        )

        # GRANTS
        training_table.grant_read_write_data(create_throw)
        training_table.grant_read_write_data(score_throws)
        training_table.grant_read_write_data(generate_analysis)
        training_table.grant_read_data(get_series)

        bucket.grant_put(generate_analysis)

        curve_interpolate.grant_invoke(generate_analysis)

        # example resource
        # queue = sqs.Queue(
        #     self, "PocQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
