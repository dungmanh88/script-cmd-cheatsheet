terraform destroy -auto-approve
terraform apply -auto-approve
terraform plan - to preview what would make changes
terraform init - init .terraform folder
terraform graph
terraform output # query current resource attr - you must define output resource in tf file
terraform output OUTPUT_NAME # query current resource attr

terraform show # show all resources provisioned

# refer via: provider_type.name.attr

terraform apply -auto-approve -state=local
-> state local:  local.backup va local
