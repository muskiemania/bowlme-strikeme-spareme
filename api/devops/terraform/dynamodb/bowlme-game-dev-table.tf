resource "aws_dynamodb_table" "bowlme-game-dev" {
	name         = "bowlme-game-dev"
	billing_mode = "PAY_PER_REQUEST"
  	hash_key     = "game_id"
	range_key    = "pile_name"
  	attribute {
    		name = "game_id"
    		type = "S"
  	}
	attribute {
		name = "pile_name"
		type = "S"
	}
	ttl {
		attribute_name = "expires_at"
		enabled        = "true"
	}
}
