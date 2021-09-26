resource "aws_dynamodb_table" "bowlme-leaderboard-dev" {
	name         = "bowlme-leaderboard-dev"
	billing_mode = "PAY_PER_REQUEST"
  	hash_key     = "game_id"
	range_key    = "rank"
  	attribute {
    		name = "game_id"
    		type = "S"
  	}
	attribute {
		name = "rank"
		type = "N"
	}
	ttl {
		attribute_name = "expires_at"
		enabled        = "true"
	}
}
