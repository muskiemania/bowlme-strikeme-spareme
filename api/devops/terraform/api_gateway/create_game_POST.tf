resource "aws_apigatewayv2_integration" "bowlme-v2-lambda-create-game-integration" {
	api_id           = aws_apigatewayv2_api.bowlme-v2-lambda-api.id
    	integration_type = "AWS_PROXY"

    	integration_method   = "POST"
    	integration_uri      = var.bowlme_v2_create_game_lambda_arn
    	passthrough_behavior = "WHEN_NO_MATCH"
}

resource "aws_apigatewayv2_route" "lambda-route" {
	api_id             = aws_apigatewayv2_api.bowlme-v2-lambda-api.id
	route_key          = "POST /game/create"
	target             = "integrations/${aws_apigatewayv2_integration.bowlme-v2-lambda-create-game-integration.id}"
}

resource "aws_lambda_permission" "api-gw" {
	statement_id  = "AllowExecutionFromAPIGateway"
	action        = "lambda:InvokeFunction"
	function_name = var.bowlme_v2_create_game_lambda_arn
	principal     = "apigateway.amazonaws.com"
	source_arn    = "${aws_apigatewayv2_api.bowlme-v2-lambda-api.execution_arn}/*/*/*"
}
