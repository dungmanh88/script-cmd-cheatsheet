sudo cryptsetup luksOpen /dev/sdb1 MyBackup
sudo mount /dev/mapper/MyBackup  /mnt
sudo umount /mnt
sudo cryptsetup luksClose  MyBackup
