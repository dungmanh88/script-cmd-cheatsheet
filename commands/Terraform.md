terraform destroy -auto-approve # automatically refresh
terraform apply -auto-approve # automatically refresh
terraform plan - to preview what would make changes
terraform init - init .terraform folder
terraform graph
terraform output # query current resource attr - you must define output resource in tf file
terraform output OUTPUT_NAME # query current resource attr

terraform plan -out=tfplan # output tf plan to a binary file
terraform show tfplan # view tf plan in human reable text
terraform apply tfplan # apply from tf plan
terraform plan -destroy -out tf-destroy-plan # plan to destroy
Destroy can't be called with a plan file -> wrong: terraform destroy tf-destroy-plan

terraform show # show all resources provisioned

# refer via: provider_type.name.attr

terraform apply -auto-approve -state=local
-> state local:  local.backup va local

terraform refresh: update existing aws on aws to tfstate (remote|local)
like: remove a resource or modify a resource

Terraform automatically discovers provider requirements from your
configuration, including providers used in child modules. To see the
requirements and constraints from each module, run "terraform providers".

provider o day la aws - cloud provider, do terraform work with many cloud providers.
provider installed when run terraform init.
