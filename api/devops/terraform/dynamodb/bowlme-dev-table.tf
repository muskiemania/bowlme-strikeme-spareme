resource "aws_dynamodb_table" "bowlme-dev" {
	name         = "bowlme-dev"
	billing_mode = "PAY_PER_REQUEST"
  	hash_key     = "game_id"
  	attribute {
    		name = "game_id"
    		type = "S"
  	}

	ttl {
		attribute_name = "expires_at"
		enabled        = "true"
	}
}
