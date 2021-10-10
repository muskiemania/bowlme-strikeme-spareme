resource "aws_lambda_function" "bowlme-discard-cards" {
	function_name    = "bowlme-v2-us-west-2-discard-cards"
  	s3_bucket        = "bowlme-cicd"
  	s3_key           = "v2/discard_cards.zip"
  	source_code_hash = filebase64sha256("../../s3/discard_cards.zip")
	role             = var.bowlme_lambda_role_arn
  	handler          = "discard_cards.handler"
  	runtime          = "python3.8"

	environment {
		variables = {
			"environ" = "dev"
		}
	}
}

