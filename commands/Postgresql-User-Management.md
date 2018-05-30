# Always lock account postgres
https://serverfault.com/questions/110154/whats-the-default-superuser-username-password-for-postgres-after-a-new-install/325596#325596
```
passwd -l postgres
```

# Connect to postgresql server
```
su - postgres
psql
```
or
```
sudo -u postgres psql postgres
connect to postgres db in postgresql server using username postgres via psql program
```

# Get version
```
postgres=# select version();
                                                 version
----------------------------------------------------------------------------------------------------------
 PostgreSQL 9.6.7 on x86_64-pc-linux-gnu, compiled by gcc (GCC) 4.8.5 20150623 (Red Hat 4.8.5-16), 64-bit
(1 row)
```

# Get server encoding
```
postgres=# show server_encoding;
 server_encoding
-----------------
 UTF8
(1 row)
```

# Show databases
```
postgres=# \l
                                  List of databases
   Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges
-----------+----------+----------+-------------+-------------+-----------------------
 postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
 template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
(3 rows)
```

# Use database
```
postgres-# \connect postgres
You are now connected to database "postgres" as user "postgres".
```

# Show tables
```
postgres=# \dt
No relations found.
```

# Show schema
```
postgres=# \dn
  List of schemas
  Name  |  Owner
--------+----------
 public | postgres
(1 row)
```

# Show roles
```
postgres=# \du
                                   List of roles
 Role name |                         Attributes                         | Member of
-----------+------------------------------------------------------------+-----------
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
```

## Create and alter user
http://www.postgresqltutorial.com/postgresql-administration/
```
postgres=# CREATE USER sonar WITH PASSWORD 'passwd';
user is created using create user will have login right

postgres=# alter user postgres with password 'passwd';

CREATE DATABASE sonar with owner sonar encoding 'UTF8'
By default, the database will use public schema.
```

# Peer vs md5 authentication
https://stackoverflow.com/questions/18664074/getting-error-peer-authentication-failed-for-user-postgres-when-trying-to-ge

# Quit
```
\q   
```
