# Rescan additional vmware disk without reboot
```
ls /sys/class/scsi_host
echo "- - -" > /sys/class/scsi_host/host0/scan
echo "- - -" > /sys/class/scsi_host/host1/scan
echo "- - -" > /sys/class/scsi_host/host2/scan
fdisk -l
```

# Create filesystem on a partition
```
mkfs.ext4 /dev/sdb1
```

# Get UUID
```
blkid
```

# Automount
```
/etc/fstab
```
