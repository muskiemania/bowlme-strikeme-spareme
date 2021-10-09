resource "aws_sns_topic" "bowlme-v2-scoring" {
	name            = "bowlme-v2-us-west-2-scoring"
	delivery_policy = <<EOF
	{
		"http": {
			"defaultHealthyRetryPolicy": {
				"minDelayTarget": 20,
				"maxDelayTarget": 20,
				"numRetries": 3,
				"numMaxDelayRetries": 0,
				"numNoDelayRetries": 0,
				"numMinDelayRetries": 0,
				"backoffFunction": "linear"
			},
			"disableSubscriptionOverrides": false,
			"defaultThrottlePolicy": {
				"maxReceivesPerSecond": 1
			}
		}
	}
	EOF
}

resource "aws_sns_topic_policy" "score_hand_policy" {
	arn    = aws_sns_topic.bowlme-v2-scoring.arn
	policy = data.aws_iam_policy_document.scoring_sns_topic_policy.json
}

resource "aws_sns_topic_subscription" "invoke_score_hand_lambda" {
	topic_arn = aws_sns_topic.bowlme-v2-scoring.arn
	protocol  = "lambda"
	endpoint  = var.bowlme-v2-score-hand-lambda-function-arn

	filter_policy = <<EOF
	{
		"MODE": ["SCORE_HAND"]
	}
	EOF
}

resource "aws_lambda_permission" "allow_sns_invoke_score_hand" {
	statement_id  = "AllowExecutionFromSNS"
	action        = "lambda:InvokeFunction"
	function_name = var.bowlme-v2-score-hand-lambda-function-name
	principal     = "sns.amazonaws.com"
	source_arn    = aws_sns_topic.bowlme-v2-scoring.arn
}
