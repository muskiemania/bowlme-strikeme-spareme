resource "aws_lambda_function" "bowlme-create-qr-code" {
	function_name    = "bowlme-v2-us-west-2-create-qr-code"
  	s3_bucket        = "bowlme-cicd"
  	s3_key           = "v2/create_qr_code.zip"
  	source_code_hash = filebase64sha256("../../s3/create_qr_code.zip")
	role             = var.bowlme_lambda_role_arn
  	handler          = "create_qr_code.handler"
  	runtime          = "python3.8"

	environment {
		variables = {
			"environ" = "dev"
		}
	}
}

