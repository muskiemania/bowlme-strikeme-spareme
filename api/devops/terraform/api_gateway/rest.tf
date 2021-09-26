resource "aws_api_gateway_rest_api" "bowlme-create-game" {
	name = "bowlme-create-game"
}

resource "aws_api_gateway_resource" "game" {
  	parent_id   = aws_api_gateway_rest_api.bowlme-create-game.root_resource_id
  	path_part   = "game"
  	rest_api_id = aws_api_gateway_rest_api.bowlme-create-game.id
}

resource "aws_api_gateway_resource" "create" {
  	parent_id   = aws_api_gateway_resource.game.id
  	path_part   = "create"
  	rest_api_id = aws_api_gateway_rest_api.bowlme-create-game.id
}

resource "aws_api_gateway_method" "create" {
  	authorization = "NONE"
  	http_method   = "POST"
  	resource_id   = aws_api_gateway_resource.create.id
  	rest_api_id   = aws_api_gateway_rest_api.bowlme-create-game.id
}

resource "aws_api_gateway_method_response" "method_response_200" {
	rest_api_id = aws_api_gateway_rest_api.bowlme-create-game.id
  	resource_id = aws_api_gateway_resource.create.id
  	http_method = aws_api_gateway_method.create.http_method
  	status_code = "200"
}

resource "aws_api_gateway_integration_response" "integration_response_200" {
	rest_api_id = aws_api_gateway_rest_api.bowlme-create-game.id
	resource_id = aws_api_gateway_resource.create.id
	http_method = aws_api_gateway_method.create.http_method
	status_code = aws_api_gateway_method_response.method_response_200.status_code

	response_templates = {
		"application/json" = <<EOF
			#set ($bodyObj = $util.parseJson($input.body))
        		#if ($bodyObj.status == "SUCCEEDED")
    				#set ($body = $util.parseJson($bodyObj.output))
    				$body.body
			#elseif ($bodyObj.status == "FAILED")
    				#set($context.responseOverride.status = 500)
    				{
        				"cause": "$bodyObj.cause",
        				"error": "$bodyObj.error"
    				}
			#else
    				#set($context.responseOverride.status = 500)
    				$input.body
			#end
		EOF
	}
}


resource "aws_api_gateway_integration" "proxy-to-sfn" {
  	http_method             = aws_api_gateway_method.create.http_method
  	integration_http_method = aws_api_gateway_method.create.http_method
	resource_id             = aws_api_gateway_resource.create.id
  	rest_api_id             = aws_api_gateway_rest_api.bowlme-create-game.id
  	type                    = "AWS"
	passthrough_behavior    = "WHEN_NO_MATCH"
	credentials             = "arn:aws:iam::359299993558:role/bowlme_sfn_role"
	uri                     = "arn:aws:apigateway:us-west-2:states:action/StartSyncExecution"

	request_templates       = {
		"application/json" = <<EOF
			{
				"input": "$util.escapeJavaScript($input.body)",
				"stateMachineArn": "arn:aws:states:us-west-2:359299993558:stateMachine:bowlme-v2-us-west-2-create-game"
			}
		EOF
	}
}

resource "aws_api_gateway_deployment" "bowlme-create" {
  	rest_api_id = aws_api_gateway_rest_api.bowlme-create-game.id

  	triggers = {
    	# NOTE: The configuration below will satisfy ordering considerations,
    	#       but not pick up all future REST API changes. More advanced patterns
    	#       are possible, such as using the filesha1() function against the
    	#       Terraform configuration file(s) or removing the .id references to
    	#       calculate a hash against whole resources. Be aware that using whole
    	#       resources will show a difference after the initial implementation.
    	#       It will stabilize to only change when resources change afterwards.
    		redeployment = sha1(jsonencode([
      			aws_api_gateway_resource.create.id,
      			aws_api_gateway_method.create.id,
      			aws_api_gateway_integration.proxy-to-sfn.id,
			aws_api_gateway_method_response.method_response_200,
    			aws_api_gateway_integration_response.integration_response_200
		]))
  	}

  	lifecycle {
    		create_before_destroy = true
  	}
}

resource "aws_api_gateway_stage" "dev" {
  	deployment_id = aws_api_gateway_deployment.bowlme-create.id
  	rest_api_id   = aws_api_gateway_rest_api.bowlme-create-game.id
  	stage_name    = "dev"
}
