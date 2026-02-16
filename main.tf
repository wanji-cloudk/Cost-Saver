provider "aws" {
    region = "us-east-1"
}

resource "aws_instance" "wanji_server" {
    ami           = "ami-0c55b159cbfafe1f0" # Amazon Linux 2
    instance_type = "t2.micro"
    tags = {
      Name = "wanjiServer-Protected"
      project = "Main"
    } 
}

resource "aws_instance" "wanji2_server" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  tags = {
    Name = "Temporary-Server"
  }
}
