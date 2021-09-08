variable "bowlme_v2_create_game_lambda_arn" {
	description = "arn for create_game lambda"
	type        = string
	default     = "arn:aws:lambda:us-west-2:359299993558:function:bowlme-v2-us-west-2-create-game"
}

variable "bowlme_v2_create_player_lambda_arn" {
	description = "arn for create_player lambda"
	type        = string
	default     = "arn:aws:lambda:us-west-2:359299993558:function:bowlme-v2-us-west-2-create-player"
}
