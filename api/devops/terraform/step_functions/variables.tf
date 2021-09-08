variable "bowlme_stepfunction_role_arn" {
	description = "execution role for bowlme step functions"
	type        = string
	default     = "arn:aws:iam::359299993558:role/bowlme_sfn_role"
}
