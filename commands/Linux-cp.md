# Copy all include hidden file/folder
```
cp -r /source/folder/. /dest/folder
```

# Copy overwrite
```
cp -Tr /source/folder /source/folder.bak
```

But if you copy:
```
cp -r /source/folder /source/folder.bak
```
you will see folder in /source/folder.bak
```
cd /source/folder.bak
ls
drwxr-xr-x. 2 root root   30 Jul 21 11:31 .
dr-xr-x---. 8 root root 4096 Jul 21 11:29 ..
-rw-r--r--. 1 root root 1166 Jul 21 11:31 folder
```
Or if you copy:
```
cp -r /source/folder/ /source/folder.bak
```
you will see content of /source/folder/ in /source/folder.bak

**By default, cp -r /source/folder/ /source/folder.bak or cp -r /source/folder/* /source/folder.bak not include hidden files/directories.**

For more clear, you just use
```
cp -r /source/folder/. /dest/folder -> copy all, include hidden content.
cp -r /source/folder/* /dest/folder -> copy non-hidden content.
cp -Tr /source/folder/ /source/folder.bak -> copy overwrite folder.
```
