from aws_cdk import (
        Stack,
        aws_apigatewayv2_alpha as apigw2a,
        aws_apigatewayv2_authorizers_alpha as apigw2aa,
        aws_apigatewayv2_integrations_alpha as apigw2a_int,
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
        authorizer_lambda = _python.PythonFunction(
                self,
                'Authorizer',
                entry='lambda',
                runtime=_lambda.Runtime.PYTHON_3_8,
                layers=[jwt_layer],
                index='authorize.py',
                handler='handler',
                environment={
                    'DYNAMODB': json.dumps({
                        'games_table': {
                            'table_name': _games_table.table_name},
                        'players_table': {
                            'table_name': _players_table.table_name}})})

        whoami_lambda = _python.PythonFunction(
                self,
                'WhoAmI',
                entry='lambda',
                runtime=_lambda.Runtime.PYTHON_3_8,
                index='whoami.py',
                handler='handler')

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
                    'DYNAMODB': json.dumps({
                        'games_table': {
                            'table_name': _games_table.table_name}}),
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

        # API GATEWAY
        http_api = apigw2a.HttpApi(
                self,
                'BowlApi',
                description='Bowl API',
                cors_preflight=apigw2a.CorsPreflightOptions(
                    allow_headers=[
                        'authorization',
                        'content-type',
                        'x-amz-date',
                        'x-amz-security-token',
                        'x-api-key',
                        'accept'],
                    allow_methods=[apigw2a.CorsHttpMethod.ANY],
                    allow_origins=['*']))

        # INTEGRATIONS
        whoami_alias = _lambda.Alias(
                self,
                'WhoAmILambdaAlias',
                alias_name=f'local-{whoami_lambda.current_version.version}',
                version=whoami_lambda.current_version)

        whoami_integration = apigw2a_int.HttpLambdaIntegration(
                'WhoAmILambdaIntegration',
                handler=whoami_alias)

        create_game_alias = _lambda.Alias(
                self,
                'CreateGameLambdaAlias',
                alias_name=f'local-{create_game_lambda.current_version.version}',
                version=create_game_lambda.current_version)

        create_game_integration = apigw2a_int.HttpLambdaIntegration(
                'CreateGameLambdaIntegration',
                handler=create_game_alias)

        join_game_alias = _lambda.Alias(
                self,
                'JoinGameLambdaAlias',
                alias_name=f'local-{join_game_lambda.current_version.version}',
                version=join_game_lambda.current_version)

        join_game_integration = apigw2a_int.HttpLambdaIntegration(
                'JoinGameLambdaIntegration',
                handler=join_game_alias)

        game_status_alias = _lambda.Alias(
                self,
                'GameStatusLambdaAlias',
                alias_name=f'local-{game_status_lambda.current_version.version}',
                version=game_status_lambda.current_version)

        game_status_integration = apigw2a_int.HttpLambdaIntegration(
                'GameStatusLambdaIntegration',
                handler=game_status_alias)

        draw_cards_alias = _lambda.Alias(
                self,
                'DrawCardsLambdaAlias',
                alias_name=f'local-{draw_cards_lambda.current_version.version}',
                version=draw_cards_lambda.current_version)

        draw_cards_integration = apigw2a_int.HttpLambdaIntegration(
                'DrawCardsLambdaIntegration',
                handler=draw_cards_alias)

        discard_cards_alias = _lambda.Alias(
                self,
                'DiscardCardsLambdaAlias',
                alias_name=f'local-{discard_cards_lambda.current_version.version}',
                version=discard_cards_lambda.current_version)

        discard_cards_integration = apigw2a_int.HttpLambdaIntegration(
                'DiscardCardsLambdaIntegration',
                handler=discard_cards_alias)

        # AUTHORIZERS
        bowl_authorizer = apigw2aa.HttpLambdaAuthorizer(
                'BowlAuthorizer',
                handler=authorizer_lambda,
                response_types=[apigw2aa.HttpLambdaResponseType.IAM])

        # ROUTES
        http_api.add_routes(
                path='/game/create',
                methods=[apigw2a.HttpMethod.POST],
                integration=create_game_integration)

        http_api.add_routes(
                path='/game/join',
                methods=[apigw2a.HttpMethod.POST],
                integration=join_game_integration)

        http_api.add_routes(
                path='/game/status',
                methods=[apigw2a.HttpMethod.POST],
                integration=game_status_integration,
                authorizer=bowl_authorizer)

        http_api.add_routes(
                path='/game/whoami',
                methods=[apigw2a.HttpMethod.GET],
                integration=whoami_integration,
                authorizer=bowl_authorizer)

        http_api.add_routes(
                path='/game/cards/draw',
                methods=[apigw2a.HttpMethod.POST],
                integration=draw_cards_integration,
                authorizer=bowl_authorizer)

        http_api.add_routes(
                path='/game/cards/discard',
                methods=[apigw2a.HttpMethod.POST],
                integration=discard_cards_integration,
                authorizer=bowl_authorizer)
      
        # GRANTS
        _games_table.grant_read_data(authorizer_lambda)
        _games_table.grant_read_write_data(create_game_lambda)
        _games_table.grant_read_data(join_game_lambda)
        _games_table.grant_read_data(game_status_lambda)
        _games_table.grant_read_write_data(draw_cards_lambda)
        _games_table.grant_read_write_data(discard_cards_lambda)
 
        _players_table.grant_read_data(authorizer_lambda)
        _players_table.grant_read_write_data(create_game_lambda)
        _players_table.grant_read_write_data(join_game_lambda)
        _players_table.grant_read_write_data(draw_cards_lambda)
        _players_table.grant_read_write_data(discard_cards_lambda)

        _event_bus.grant_put_events_to(create_game_lambda)
        _event_bus.grant_put_events_to(game_status_lambda)
        _event_bus.grant_put_events_to(draw_cards_lambda)
        _event_bus.grant_put_events_to(discard_cards_lambda)
