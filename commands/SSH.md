# disable host checking
ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking
# use ssh config
ssh -F another-config-file (global: /etc/ssh/ssh_config, each user: ~/.ssh/config)
