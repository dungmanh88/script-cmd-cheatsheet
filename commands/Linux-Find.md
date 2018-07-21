https://stackoverflow.com/questions/4210042/how-to-exclude-a-directory-in-find-command
Print all directory in  current directory exclude ./bin
```
find . -path ./bin -prune -o -type d -print
```

Print all directory in $HOME exclude $HOME/bin
```
find $HOME -path $HOME/bin -prune -o -type d -print
```

Don't use:
```
find $HOME -path ./bin -prune -o -type d -print
or
find . -path $HOME/bin -prune -o -type d -print
```

If you want to exclude many directories:
```
find . \( -path ./bin -o -path ./tmp -o -path ./cmd/cmd1 \) -prune -o -type d -print
```
find command still recursive finding but exclude ./bin, ./tmp and ./cmd/cmd1 from final result.

You also extend for all files and directories.

If you want to do something on final result that find return:
```
find . -path ./bin -prune -o -name "*.sh"  -exec cp {} ./bin \;
```
copy all files .sh to ./bin
don't copy file in ./bin to ./bin -> prevent loop.
