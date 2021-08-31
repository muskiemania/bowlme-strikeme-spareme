variable "bowlme_lambda_role_arn" {
	description = "execution role for bowlme lambdas"
	type        = string
	default     = "arn:aws:iam::359299993558:role/bowlme_lambda_assume_role"
}
