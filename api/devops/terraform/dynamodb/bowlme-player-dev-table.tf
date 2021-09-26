resource "aws_dynamodb_table" "bowlme-player-dev" {
	name         = "bowlme-player-dev"
	billing_mode = "PAY_PER_REQUEST"
  	hash_key     = "game_id"
	range_key    = "player_id"
  	attribute {
    		name = "game_id"
    		type = "S"
  	}
	attribute {
		name = "player_id"
		type = "S"
	}
	ttl {
		attribute_name = "expires_at"
		enabled        = "true"
	}
}
