# Get all processes run under a specific user
ps -u root

# Get full information
ps -ulf root

# Get everything
ps -elf

# Get pid of a process
pidof <process-name>

# How long a process has been running
ps -p <pid> -o etime,uid,gid,cmd,pid
or
ps -p <pid> -o etimes,uid,gid,cmd,pid
