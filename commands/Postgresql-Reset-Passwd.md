# Edit config md5 to trust
vi /var/lib/pgsql/9.6/data/pg_hba.conf
```
change md5 to trust
from
local   all             all                                     md5
to
local   all             all                                     trust
```

# Restart service
```
systemctl restart postgresql-9.6
```

# Change new passwd
```
su - postgres
-bash-4.2$ psql
psql (9.6.7)
Type "help" for help.

postgres=# alter user postgres with password 'passwd';
```

# Revert edit in pg_hba.conf
vi /var/lib/pgsql/9.6/data/pg_hba.conf
```
change trust to md5
from
local   all             all                                     trust
to
local   all             all                                     md5
```

# Restart service to apply
```
systemctl restart postgresql-9.6
```

# Re-login
```
su - postgres
-bash-4.2$ psql
Password:
psql (9.6.7)
Type "help" for help.

postgres=#
```
