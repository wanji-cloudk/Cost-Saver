## Cost-Saver-Terraform + boto3 project
A toolkit designed to monitor and prevent unnecessary expenses.Infrastructure as Code (Terraform): Uses main.tf to provision cost-optimized AWS environments(like t3.nano instances) with mandatory tagging. This ensures that every resource created has a "purpose" and an "owner",and automatically deploys Python-based governance scripts to scan your AWS environment and eliminate waste by automatically shutdowning instances missing a "Project" tag and Stop instances tagged for scheduled shutdown to save money and ensure you only pay for what you actually use.

## Make sure you sign up at aws.amazon.com
configure AWS:
```bash
aws configure

  AWS Access Key ID:      - your key
  AWS Secret Access Key:  - your secret
  Default region name:    -us-east-1
  Default output format:  - press Enter


## Files and what they do:
`main.tf` blueprint that tells AWS exactly what to build

`auto-stop.py` monitors and stopping everything that isn't tagged 

## Setup 
1, Install dependancies:
```bash
pip install boto3
pip install awscli

2, install Terraform
pip install python-terraform
Note: This still requires the actual Terraform binary from requirements.txt to be installed on your system first.

## Enviroment setup
Set your default AWS region 
```bash
export AWS_DEFAULT_REGION=us-east-1 

## Provision Infrustracture
First, deploy the low-cost resources defined in your Terraform files:
```bash
terraform init   - Downloads the AWS plugin so Terraform can communicate with your account.
terraform apply  - Sends the request to AWS to actually build the two servers.

## Clean up
We create a second instance but omit the Project tag. This represents a "forgotten" resource that is wasting money,Once your enviroment is active, run python script to identify and stopping everything that isn't tagged:

```bash
python auto-stop.py

##  Destroy when done
```bash
terraform destroy

#### Run Locally
clone the project

git clone [https://github.com/wanji-cloudk/Cost-Saver.git]

### Authers:
This project is developed by(https://www.github.com/wanji-cloudk)

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

### Contributing:
You are always welcome to contribute to this project and kindly submit a pull requst to any improment you've made,Your input can help make the terraform-boto3 script even better for users.






