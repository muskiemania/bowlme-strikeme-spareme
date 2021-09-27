data "aws_iam_policy_document" "shuffle_cards_sns_topic_policy" {
	policy_id = "__default_policy_ID"

	statement {
		actions = [
			"SNS:Subscribe",
			"SNS:SetTopicAttributes",
			"SNS:Receive",
			"SNS:Publish",
			"SNS:GetTopicAttributes"
		]

		condition {
			test     = "StringEquals"
			variable = "AWS:SourceOwner"

			values = [
				var.account-id
			]
		}

		effect = "Allow"
		
		principals {
			type        = "AWS"
			identifiers = ["*"]
		}

		resources = [
			aws_sns_topic.bowlme-v2-shuffle-cards.arn
		]

		sid = "__default_statement_ID"
	}
}
