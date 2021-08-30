terraform {
  backend "s3" {
    bucket  = "bowlme-cicd"
    key     = "terraform/v2.tfstate"
    region  = "us-west-1"
    profile = "tf-user"
  }
}
