#!/bin/bash

read -p "Access token: " access_token
echo "token = $access_token"
read -p "Domain: " domain
echo "domain = $domain"
curl -s -H "Private-Token: $access_token" -X PUT https://$domain/api/v4/projects/701?visibility=private
