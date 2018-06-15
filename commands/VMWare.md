# Get all running vm
```
esxcli vm process list
```

# Get all vm
```
vim-cmd vmsvc/getallvms | grep vm-name
```

# Get state of vm
```
vim-cmd vmsvc/power.getstate vm-id
get vm-id using vim-cmd vmsvc/getallvms | grep vm-name
```

# Check vmware toolbox
```
/etc/init.d/vmware-tools status
or
vmware-toolbox-cmd --version
```

# Check vmare network
```
esxcli network ip interface list
```
```
esxcli network ip interface ipv4 get
```
```
esxcli network ip dns server list
```
