resource "aws_lambda_function" "bowlme-create-player" {
	function_name    = "bowlme-v2-us-west-2-create-player"
  	s3_bucket        = "bowlme-cicd"
  	s3_key           = "v2/create_player.zip"
  	source_code_hash = filebase64sha256("../../s3/create_player.zip")
	role             = var.bowlme_lambda_role_arn
  	handler          = "create_player.handler"
  	runtime          = "python3.8"

	environment {
		variables = {
			"environ" = "dev"
		}
	}
}

resource "aws_lambda_permission" "allow-state-function-create-game" {
	statement_id  = "AllowStateMachine"
	action        = "lambda:InvokeFunction"
	function_name = aws_lambda_function.bowlme-create-player.function_name
	principal     = "states.amazonaws.com"
	source_arn    = "arn:aws:states:us-west-2:359299993558:express:bowlme-v2-us-west-2-create-game"
}

