resource "aws_instance" "broken" {
  ami           = missingGreeting
  instance_type = "t2.micro"
}
