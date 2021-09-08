resource "aws_sfn_state_machine" "bowlme-v2-create-game" {
	name     = "bowlme-v2-us-west-2-create-game"
	role_arn = var.bowlme_stepfunction_role_arn
	type     = "EXPRESS"

	definition = file("./create_game_state_machine.json")

	logging_configuration {
		log_destination = "${aws_cloudwatch_log_group.bowlme-v2-state-machine-log-group.arn}:*"
		include_execution_data = true
		level = "ERROR"
	}
}

resource "aws_cloudwatch_log_group" "bowlme-v2-state-machine-log-group" {
  	name              = "Step-Function-Execution-Logs_bowlme-v2-create-game/default"
  	retention_in_days = 7
}
