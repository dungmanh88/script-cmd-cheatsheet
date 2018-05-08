# How to setup ssh key based authentication

## Client-side
```
You are dungzz. You want to login as dungmanh on server.
ssh-keygen will generate: ~/.ssh/id_rsa and ~/.ssh/id_rsa.pub
chmod 700 ~/.ssh
chmod 400 ~/.ssh/id_rsa
chmod 644 ~/.ssh/id_rsa.pub
chown -R dungzz:dungzz ~/.ssh
```

## How to copy public key to other machine
```
Solution 1:
Copy-paste public key of dungzz to ~/.ssh/authorized_keys of dungmanh

Solution 2:
Enable PasswordAuthentication in /etc/ssh/sshd_config on server, restart sshd service to apply.
Set passwd for user dungmanh on server
From client, you run command: ssh-copy-id -i /path/to/public/key dungmanh@server-ip
Enter passwd of dungmanh that you have set
Disable PasswordAuthentication in /etc/ssh/sshd_config on server, restart sshd service to apply.
```

## Server-side
```
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
chown -R dungmanh:dungmanh ~/.ssh
```
