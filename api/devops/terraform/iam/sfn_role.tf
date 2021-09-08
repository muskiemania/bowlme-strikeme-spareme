resource "aws_iam_role_policy" "bowlme_sfn_execute_policy" {
	name = "bowlme_sfn_execute_policy"
  	role = aws_iam_role.bowlme_sfn_role.id
	policy = file("./sfn_execute_policy.json")
}

resource "aws_iam_role_policy" "bowlme_sfn_logs_policy" {
	name = "bowlme_sfn_logs_policy"
  	role = aws_iam_role.bowlme_sfn_role.id
	policy = file("./sfn_logs_policy.json")
}

resource "aws_iam_role" "bowlme_sfn_role" {
 	name = "bowlme_sfn_role"
	assume_role_policy = file("./sfn_role_policy.json")
}

