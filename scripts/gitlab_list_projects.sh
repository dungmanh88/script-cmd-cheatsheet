#!/bin/bash
read -p "Domain: " domain
echo "domain = $domain"
curl -s -X GET https://$domain/api/v4/projects?visibility=public > /tmp/public_projects.json
