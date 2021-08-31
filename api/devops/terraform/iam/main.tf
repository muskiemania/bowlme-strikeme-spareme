resource "aws_iam_role_policy" "bowlme_lambda_dynamo_policy" {
	name = "bowlme_lambda_dynamo_policy"
  	role = aws_iam_role.bowlme_lambda_assume_role.id
	policy = file("./dynamo_policy.json")
}

resource "aws_iam_role" "bowlme_lambda_assume_role" {
 	name = "bowlme_lambda_assume_role"
	assume_role_policy = file("./assume_role_policy.json")
}
