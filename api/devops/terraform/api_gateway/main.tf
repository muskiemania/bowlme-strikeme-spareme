resource "aws_apigatewayv2_api" "bowlme-v2-lambda-api" {
	name                 = "bowlme-v2-lambda-api"
	protocol_type        = "HTTP"
}

resource "aws_apigatewayv2_stage" "bowlme-v2-lambda-stage" {
	api_id      = aws_apigatewayv2_api.bowlme-v2-lambda-api.id
    	name        = "$default"
   	access_log_settings {
		destination_arn = "${aws_cloudwatch_log_group.bowlme-v2-api-log-group.arn}"
		format          = jsonencode({
        		httpMethod     = "$context.httpMethod"
        		ip             = "$context.identity.sourceIp"
        		protocol       = "$context.protocol"
        		requestId      = "$context.requestId"
        		requestTime    = "$context.requestTime"
        		responseLength = "$context.responseLength"
        		routeKey       = "$context.routeKey"
        		status         = "$context.status"
			errorMessage   = "$context.error.messageString"
      		})
	}
	auto_deploy = true
}

resource "aws_cloudwatch_log_group" "bowlme-v2-api-log-group" {
  	name              = "API-Gateway-Execution-Logs_${aws_apigatewayv2_api.bowlme-v2-lambda-api.id}/default"
  	retention_in_days = 7
}

