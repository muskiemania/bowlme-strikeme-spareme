terraform {
  	backend "s3" {
    		bucket  = "bowlme-cicd"
    		key     = "terraform/apigateway.v2.tfstate"
    		region  = "us-west-2"
    		profile = "tf-user"
  	}
}

provider "aws" {
	region  = "us-west-2"
	profile = "tf-user"
}
