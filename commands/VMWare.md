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
