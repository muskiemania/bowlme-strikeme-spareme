variable "bowlme-v2-shuffle-cards-lambda-function-name" {
	description = "shuffle cards function name"
	type        = string
	default     = "bowlme-v2-us-west-2-shuffle-cards"
}

variable "bowlme-v2-shuffle-cards-lambda-function-arn" {
	description = "shuffle cards function arn"
	type        = string
	default     = "arn:aws:lambda:us-west-2:359299993558:function:bowlme-v2-us-west-2-shuffle-cards"
}

variable "bowlme-v2-score-hand-lambda-function-name" {
	description = "score hand function name"
	type        = string
	default     = "bowlme-v2-us-west-2-score-hand"
}

variable "bowlme-v2-score-hand-lambda-function-arn" {
	description = "score hand function arn"
	type        = string
	default     = "arn:aws:lambda:us-west-2:359299993558:function:bowlme-v2-us-west-2-score-hand"
}

variable "account-id" {
	description = "my account id"
	type        = string
	default     = "359299993558"
}
