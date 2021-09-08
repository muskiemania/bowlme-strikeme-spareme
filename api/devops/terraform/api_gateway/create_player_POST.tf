resource "aws_apigatewayv2_integration" "bowlme-v2-lambda-create-player-integration" {
	api_id           = aws_apigatewayv2_api.bowlme-v2-lambda-api.id
    	integration_type = "AWS_PROXY"

    	integration_method   = "POST"
    	integration_uri      = var.bowlme_v2_create_player_lambda_arn

	response_parameters {
        	mappings    = {
              		"overwrite:header.Content-Type" = "application/json"
            	}
          	status_code = "200"
        }
}

resource "aws_apigatewayv2_route" "create-player-lambda-route" {
	api_id             = aws_apigatewayv2_api.bowlme-v2-lambda-api.id
	route_key          = "POST /game/player/create"
	target             = "integrations/${aws_apigatewayv2_integration.bowlme-v2-lambda-create-player-integration.id}"
}

resource "aws_lambda_permission" "create-player-allow-api-gateway" {
	statement_id  = "AllowExecutionFromAPIGateway"
	action        = "lambda:InvokeFunction"
      	function_name = var.bowlme_v2_create_player_lambda_arn
      	principal     = "apigateway.amazonaws.com"
      	source_arn    = "arn:aws:execute-api:us-west-2:359299993558:6ra4b3z96j/*/*/game/player/create"
}

