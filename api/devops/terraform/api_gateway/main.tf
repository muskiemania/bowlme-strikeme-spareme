resource "aws_apigatewayv2_api" "bowlme-v2-lambda-api" {
	name          = "bowlme-v2-lambda-api"
	protocol_type = "HTTP"
}

resource "aws_apigatewayv2_stage" "bowlme-v2-lambda-stage" {
	api_id      = aws_apigatewayv2_api.bowlme-v2-lambda-api.id
    	name        = "$default"
   	auto_deploy = true
}


