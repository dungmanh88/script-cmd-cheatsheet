aws configure
```
AWS Access Key ID
AWS Secret Access Key
Default region name [xxx]: current region
Default output format [json]: json
```
aws ecr describe-repositories
aws s3 ls
aws configure list


aws sns  list-subscriptions
aws sns  list-topics
aws sns list-subscriptions-by-topic --topic-arn "<arn>"

# Get account id
aws sts get-caller-identity --output text --query 'Account'
