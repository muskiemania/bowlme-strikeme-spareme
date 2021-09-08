#resource "aws_iam_role_policy" "bowlme_sfn_execute_policy" {
#	name = "bowlme_sfn_execute_policy"
#  	role = aws_iam_role.bowlme_sfn_role.id
#	policy = file("./sfn_execute_policy.json")
#}

#resource "aws_iam_role_policy" "bowlme_sfn_logs_policy" {
#	name = "bowlme_sfn_logs_policy"
#  	role = aws_iam_role.bowlme_sfn_role.id
#	policy = file("./sfn_logs_policy.json")
#}

data "aws_iam_policy" "AWSStepFunctionsFullAccess" {
	arn = "arn:aws:iam::aws:policy/AWSStepFunctionsFullAccess"
}

data "aws_iam_policy" "CloudWatchLogsFullAccess" {
	arn = "arn:aws:iam::aws:policy/CloudWatchLogsFullAccess"
}

resource "aws_iam_role" "bowlme_sfn_role" {
 	name = "bowlme_sfn_role"
	assume_role_policy = file("./sfn_role_policy.json")
}

resource "aws_iam_role_policy_attachment" "bowlme-attach-sfn-full-access" {
	role       = aws_iam_role.bowlme_sfn_role.name
	policy_arn = data.aws_iam_policy.AWSStepFunctionsFullAccess.arn
}

resource "aws_iam_role_policy_attachment" "bowlme-attach-cloudwatchlogs-full-access" {
	role       = aws_iam_role.bowlme_sfn_role.name
	policy_arn = data.aws_iam_policy.CloudWatchLogsFullAccess.arn
}

