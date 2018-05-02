# Up VM
```
vagrant up
```

# Shutdown VM
```
vagrant halt
```

# Destroy VM
```
vagrant destroy
```

# Restart VM
```
vagrant reload
```

# Update package in VM
```
vagrant reload --provision
or
vagrant provision
```

# Update box
```
vagrant box update
```

# SSH to VM
```
vagrant ssh

private key: .vagrant/machines/default/virtualbox/private_key
public key: in vagrant box /home/vagrant/.ssh/authorized_keys

or
ssh vagrant@127.0.0.1 -p 2222
```

# Get global status
```
vagrant global-status
```

# Share vagrant via ssh
```
https://ngrok.com/download
https://ngrok.com/signup
https://dashboard.ngrok.com
vagrant share --ssh
vagrant connect --ssh NAME
```

# Show ssh config
```
vagrant ssh-config
```

# Packaging to a box
```
vagrant package --base <UUID-of-vm> --output NAME
```

# View port
```
vagrant port my-machine
vagrant port
```

# Validate Vagrantfile
```
vagrant validate
```

# Init new Vagrantfile
```
vagrant init
```

# List plugin
```
vagrant plugin list
```
