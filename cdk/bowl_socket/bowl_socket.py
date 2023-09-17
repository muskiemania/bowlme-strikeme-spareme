from aws_cdk import (
        Stack,
        aws_apigatewayv2_alpha as apigw2a,
        aws_apigatewayv2_authorizers_alpha as apigw2aa,
        aws_apigatewayv2_integrations_alpha as apigw2a_int,
        aws_events as _events,
        aws_events_targets as targets,
        aws_lambda as _lambda,
        aws_lambda_python_alpha as _python
        )
from constructs import Construct
import json

class BowlSocketStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:

        _event_bus = kwargs.pop('event_bus')
        _games_table = kwargs.pop('games_table')
        _players_table = kwargs.pop('players_table')
        _bowl_authorizer = kwargs.pop('bowl_authorizer')

        super().__init__(scope, construct_id, **kwargs)

        # LAMBDA-LAYER
        #jwt_layer = _python.PythonLayerVersion(
        #        self,
        #        'JwtLayer',
        #        entry='layers/jwt_layer',
        #        compatible_runtimes=[_lambda.Runtime.PYTHON_3_8],
        #        description='PyJWTLibrary',
        #        layer_version_name='PyJWTLibrary')

        # LAMBDA
        #authorizer_lambda = _python.PythonFunction(
        #        self,
        #        'Authorizer',
        #        entry='lambda',
        #        runtime=_lambda.Runtime.PYTHON_3_8,
        #        layers=[jwt_layer],
        #        index='authorize.py',
        #        handler='handler',
        #        environment={
        #            'DYNAMODB': json.dumps({
        #                'games_table': {
        #                    'table_name': _games_table.table_name},
        #                'players_table': {
        #                    'table_name': _players_table.table_name}})})

        connect_lambda = _python.PythonFunction(
                self,
                'SocketConnect',
                entry='lambda',
                runtime=_lambda.Runtime.PYTHON_3_8,
                index='socket_connect.py',
                handler='handler')

        disconnect_lambda = _python.PythonFunction(
                self,
                'SocketDisonnect',
                entry='lambda',
                runtime=_lambda.Runtime.PYTHON_3_8,
                index='socket_disconnect.py',
                handler='handler',
                environment={
                    'EVENTBRIDGE': json.dumps({
                        'event_bus': {
                            'event_bus_name': _event_bus.event_bus_name}})})


        default_lambda = _python.PythonFunction(
                self,
                'SocketDefault',
                entry='lambda',
                runtime=_lambda.Runtime.PYTHON_3_8,
                index='socket_default.py',
                handler='handler',
                environment={
                    'EVENTBRIDGE': json.dumps({
                        'event_bus': {
                            'event_bus_name': _event_bus.event_bus_name}})})



        #create_game_lambda = _python.PythonFunction(
        #        self,
        #        'CreateGame',
        #        entry='lambda',
        #        runtime=_lambda.Runtime.PYTHON_3_8,
        #        layers=[jwt_layer],
        #        index='create_game.py',
        #        handler='handler',
        #        environment={
        #            'DYNAMODB': json.dumps({
        #                'games_table': {
        #                    'table_name': _games_table.table_name},
        #                'players_table': {
        #                    'table_name': _players_table.table_name}}),
        #            'EVENTBRIDGE': json.dumps({
        #                'event_bus': {
        #                    'event_bus_name': _event_bus.event_bus_name}})})

        # API GATEWAY
        socket_api = apigw2a.WebSocketApi(
                self,
                'BowlSocketApi',
                connect_route_options=apigw2a.WebSocketRouteOptions(
                    integration=apigw2a_int.WebSocketLambdaIntegration(
                        'ConnectIntegration',
                        connect_lambda)),
                disconnect_route_options=apigw2a.WebSocketRouteOptions(
                    integration=apigw2a_int.WebSocketLambdaIntegration(
                        'DisconnectIntegration',
                        disconnect_lambda)),
                default_route_options=apigw2a.WebSocketRouteOptions(
                    integration=apigw2a_int.WebSocketLambdaIntegration(
                        'DefaultIntegration',
                        default_lambda)))

        socket_stage = apigw2a.WebSocketStage(
                self,
                'BowlSocketStage',
                web_socket_api=socket_api,
                stage_name='ws',
                auto_deploy=True)

        # AUTHORIZERS
        #bowl_authorizer = apigw2aa.HttpLambdaAuthorizer(
        #        'BowlAuthorizer',
        #        handler=authorizer_lambda,
        #        response_types=[apigw2aa.HttpLambdaResponseType.IAM])

        # ROUTES
        #http_api.add_routes(
        #        path='/game/create',
        #        methods=[apigw2a.HttpMethod.POST],
        #        integration=create_game_integration)


        socket_register_lambda = _python.PythonFunction(
                self,
                'SocketRegister',
                entry='lambda',
                runtime=_lambda.Runtime.PYTHON_3_8,
                index='socket_register.py',
                handler='handler',
                environment={
                    'DYNAMODB': json.dumps({
                        'players_table': {
                            'table_name': _players_table.table_name}})})

        socket_disconnect_lambda = _python.PythonFunction(
                self,
                'SocketDisconnect2',
                entry='lambda',
                runtime=_lambda.Runtime.PYTHON_3_8,
                index='socket_disconnect2.py',
                handler='handler',
                environment={
                    'DYNAMODB': json.dumps({
                        'players_table': {
                            'table_name': _players_table.table_name},
                        'socket_index': {
                            'index_name': 'SocketConnectionIndex'}})})



        # GRANTS
        _players_table.grant_read_write_data(socket_register_lambda)
        _players_table.grant_read_write_data(socket_disconnect_lambda)
        _event_bus.grant_put_events_to(disconnect_lambda)
        _event_bus.grant_put_events_to(default_lambda)
        #_event_bus.grant_put_events_to(game_status_lambda)
 
        # EVENT BRIDGE RULES
        _socket_register_rule = _events.Rule(
                self,
                'BowlSocketRegister',
                event_bus=_event_bus)

        _socket_register_rule.add_event_pattern(
                source=['bowlsocket.register'])
        _socket_register_rule.add_target(
                targets.LambdaFunction(socket_register_lambda))

        _socket_disconnect_rule = _events.Rule(
                self,
                'BowlSocketDisconnect',
                event_bus=_event_bus)

        _socket_disconnect_rule.add_event_pattern(
                source=['bowlsocket.disconnect'])
        _socket_disconnect_rule.add_target(
                targets.LambdaFunction(socket_disconnect_lambda))



