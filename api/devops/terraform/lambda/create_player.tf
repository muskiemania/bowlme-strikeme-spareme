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
