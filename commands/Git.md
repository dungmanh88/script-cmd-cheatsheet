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

# .gitignore
```
You can put a .gitignore at the top-level of project folder also put in a subdirectory to apply
ignore for this subdirectory and all elements of it.
```

# Three-tree architecture
```
working tree(untracked) -git add-> staging index tree(tracked) -git commit-> local repository tree [-git push-> remote repository]
git work with a set of changes on many files not a single change or a single file or multiple files
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

# Git HEAD
```
HEAD is a pointer that always points to the last commit of the currently checked out branch
by default, HEAD points to the last commit of the master branch. If you switch branch, HEAD will switch to the
last commit of new branch.
```
```
cat .git/HEAD
ref: refs/heads/master

cat .git/refs/heads/master
d977709edd76b5de814954597240f21053514929

git log HEAD
commit d977709edd76b5de814954597240f21053514929 (HEAD -> master, origin/master)
```

# Adding to staging index
```
git add <file/folder>
git add .
git add also apply changes to staging index tree.
```

# Remove file/directory
```
git rm -r <directory>
git rm <file>

git rm same as rm in linux. It also removes file/folder on file system.
git rm also apply changes to staging index tree.
```

# Rename/move file/directory
```
git mv <file/directory>
git mv also apply changes to staging index tree.
```

# Unstage
```
git reset HEAD <file/folder>
```

# Revert changes in file/folder in working tree, before add to staging index
```
git checkout <file/folder>
```

# Get status of file/folder in staging index
```
git status

On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)
Changes to be committed:  ### STAGED
  (use "git reset HEAD <file>..." to unstage)

	new file:   2

Changes not staged for commit: ### NOT STAGED
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   1

```

# Get difference version between working tree and local repository tree
```
git diff <directory>
git diff cannot see new files. It only sees the diff on a edited files.

diff --git a/1 b/1
index e69de29..d1cb2dc 100644
--- a/1 ### old version
+++ b/1 ### new version
@@ -0,0 +1,3 @@ ### add to line 1 and line 3
+123
+
+321
```

# Get difference between working tree and staging index tree
```
git diff --staged
git diff --staged can see new files.
```

# Get diff between two branches
```
git diff branch1..branch2
or use url
https://domain-name/namepsace/project-name/compare
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

# Commit to local repository tree
```
git commit -m "messge"
```

# Push to remote repository tree
```
git push origin master
```

# Manage origin
```
git remote show origin
git remote set-url origin git@github.com:dungnm-nal/github-pipeline-example.git
git remote -v
```

# Checkout branch
```
git fetch
git branch -v
git checkout <branch-name>
```

# Show remote branch
```
git remote show origin
Notice:   Remote branches
```

# Get fetch vs git pull
```
https://stackoverflow.com/questions/292357/what-is-the-difference-between-git-pull-and-git-fetch

https://i.stack.imgur.com/nWYnQ.png
```
