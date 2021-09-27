resource "aws_sns_topic" "bowlme-v2-shuffle-cards" {
	name            = "bowlme-v2-us-west-2-shuffle-cards"
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

resource "aws_sns_topic_subscription" "invoke_shuffle_cards_lambda" {
	topic_arn = aws_sns_topic.bowlme-v2-shuffle-cards.arn
	protocol  = "lambda"
	endpoint  = var.bowlme-v2-shuffle-cards-lambda-function-arn
}

resource "aws_lambda_permission" "allow_sns_invoke" {
	statement_id  = "AllowExecutionFromSNS"
	action        = "lambda:InvokeFunction"
	function_name = var.bowlme-v2-shuffle-cards-lambda-function-name
	principal     = "sns.amazonaws.com"
	source_arn    = aws_sns_topic.bowlme-v2-shuffle-cards.arn
}
