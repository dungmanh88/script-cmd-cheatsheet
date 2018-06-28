# How to find out the diff
```
diff -x <exclude-file-1> -x <exclude-file-2> -x <exclude-folder-1> -x <exclude-folder-2> -r <src> <dest>
```

# Copy all include hidden file/folder
```
cp -r /source/folder/. /dest/folder
```

# Copy overwrite
```
cp -Tr /source/folder /source/folder.bak
```

# Set hostname
```
hostnamectl set-hostname web-performance
```
