resource "aws_lambda_function" "bowlme-score-hand" {
	function_name    = "bowlme-v2-us-west-2-score-hand"
  	s3_bucket        = "bowlme-cicd"
  	s3_key           = "v2/score_hand.zip"
  	source_code_hash = filebase64sha256("../../s3/score_hand.zip")
	role             = var.bowlme_lambda_role_arn
  	handler          = "score_hand.handler"
  	runtime          = "python3.8"

	environment {
		variables = {
			"environ" = "dev"
		}
	}
}

