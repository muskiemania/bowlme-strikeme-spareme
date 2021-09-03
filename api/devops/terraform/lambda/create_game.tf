resource "aws_lambda_function" "bowlme-create-game" {
	function_name    = "bowlme-v2-us-west-2-create-game"
  	s3_bucket        = "bowlme-cicd"
  	s3_key           = "v2/create_game.zip"
  	source_code_hash = filebase64sha256("../../s3/create_game.zip")
	role             = var.bowlme_lambda_role_arn
  	handler          = "create_game.handler"
  	runtime          = "python3.8"

	environment {
		variables = {
			"environ" = "dev"
		}
	}
}
