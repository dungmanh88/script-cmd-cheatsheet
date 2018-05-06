# Config git
```
git config user.name "xxx"
git config user.email "xxx"
git config --global user.name "xxx"
git config --global user.email "xxx"
```

# Get config git
```
git config user.name
git config user.email
or view .git/config
```

# Remove file/directory
```
git rm -r <directory>
git rm <file>
git commit -m "message"
git push origin master
```

git stash: store diff in local to stack -> make clean local repo

git pull

git stash pop: flush diff in local stack to local repo after git stash

# Where Git files are stored
```
There is a .git directory in top-level directory of a project
.git contains tracking information of files and folders in the project
If you remove .git directory, git will stop tracking your project.
You don't want to modify any files or folders in .git
The only exception is .git/config file
You can read or edit the file for your purpose.
```

# Init git
```
rm -rf .git if it is exists
git init to create new .git
```

# Get history
```
git log
git log -n <limit commit object>
git log | head -n <limit output lines from top-down>
git log | tail -n <limit output lines from bottom-up>
git log --author="email|name"
git log --since=yyyy1-mm1-dd1 --until=yyyy2-mm2-dd2 (find log in a range >= yyyy1-mm1-dd1 and <= yyyy2-mm2-dd2 )
git log --grep "text in message commit"
```

# .gitignore
```
You can put a .gitignore at the top-level of project folder also put in a subdirectory to apply
ignore for this subdirectory and all elements of it.
```

# git architecture
```
working directory -git add-> staging index -git commit-> local repository -git push-> remote repository
git work with a set of changes on many files not a single change or a single file
```

# Understanding git object
```
git object or a commit object is a snapshot. It means a set of data changes on a project
The metadata of git object always refer to the previous git object.
Git object contains: commit id + author + message + date + metadata
commit id is 40 charactered (a-f0-9) hash value. It is unique. It is a result of checksum using SHA-1 algorithm
that convert data into a simple number. Same data always equals same checksum. Changing data would change checksum
Data integrity is fundamental of git
```
