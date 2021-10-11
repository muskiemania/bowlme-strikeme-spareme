resource "aws_iam_role_policy" "bowlme_lambda_dynamo_policy" {
	name = "bowlme_lambda_dynamo_policy"
  	role = aws_iam_role.bowlme_lambda_role.id
	policy = file("./dynamo_policy.json")
}

resource "aws_iam_role_policy" "bowlme_lambda_sns_policy" {
	name = "bowlme_lambda_sns_policy"
  	role = aws_iam_role.bowlme_lambda_role.id
	policy = file("./sns_policy.json")
}

resource "aws_iam_role_policy" "bowlme_lambda_s3_policy" {
	name = "bowlme_lambda_s3_policy"
  	role = aws_iam_role.bowlme_lambda_role.id
	policy = file("./s3_policy.json")
}

resource "aws_iam_role" "bowlme_lambda_role" {
 	name = "bowlme_lambda_role"
	assume_role_policy = file("./lambda_role_policy.json")
}

data "aws_iam_policy" "AWSLambdaBasicExecutionRole" {
	arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_iam_role_policy_attachment" "basic_execution_attach" {
  	role        = aws_iam_role.bowlme_lambda_role.name
  	policy_arn  = "${data.aws_iam_policy.AWSLambdaBasicExecutionRole.arn}"
}
