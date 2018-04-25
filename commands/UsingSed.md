txtfile
```
This is a text file
has an important information
ManhDung is so handsome
and many girls like him
```

sed is a stream editor that work line by line

sed does not change input file. You must use -i to edit in-place

# Append a text after lines
```
sed "a tag-after-line" /tmp/txtfile
This is a text file
tag-after-line
has an important information
tag-after-line
ManhDung is so handsome
tag-after-line
and many girls like him
tag-after-line
```

# Insert a text before lines
```
sed "i tag-before-line" /tmp/txtfile
tag-before-line
This is a text file
tag-before-line
has an important information
tag-before-line
ManhDung is so handsome
tag-before-line
and many girls like him
```

# Append a text after a specific line
```
sed "3a tag-after-line" /tmp/txtfile
This is a text file
has an important information
ManhDung is so handsome
tag-after-line
and many girls like him
```

# Append a text after a specific line using regex pattern
```
sed "/ManhDung/a \!" /tmp/txtfile
This is a text file
has an important information
ManhDung is so handsome
!
and many girls like hi
```

# Insert a text before a specific line
```
sed "3i tag-before-line" /tmp/txtfile
This is a text file
has an important information
tag-before-line
ManhDung is so handsome
and many girls like him
```

# Insert a text before a specific line using regex pattern
```
sed "/ManhDung/i %%%" /tmp/txtfile
This is a text file
has an important information
%%%
ManhDung is so handsome
and many girls like him
```

# Delete all lines
```
sed "d" /tmp/txtfile
```

# Delete a specific line
```
sed "2d" /tmp/txtfile
This is a text file
ManhDung is so handsome
and many girls like him
```

# Delete a line using regex pattern
```
sed "/ManhDung/d" /tmp/txtfile
This is a text file
has an important information
and many girls like him
```

# Using regex for searching
```
sed "/^[A-Z]/a CAPS LETTER" /tmp/txtfile
This is a text file
CAPS LETTER
has an important information
ManhDung is so handsome
CAPS LETTER
and many girls like him
```

# Remove blank lines
```
This is a text file

has an important information

ManhDung is so handsome
and many girls like him
```
```
[root@dungnm-test2 ~]# sed "/^\s*$/d" /tmp/txtfile
This is a text file
has an important information
ManhDung is so handsome
and many girls like him
```

# Replace a text at first
```
sed  "s/ManhDung is/I am/" /tmp/txtfile
This is a text file
has an important information
I am so handsome
and many girls like him

Don't lose last / in sed command
```

# Replace text greedy
```
sed  "s/[a-c]/@/g" /tmp/txtfile
This is @ text file
h@s @n import@nt inform@tion
M@nhDung is so h@ndsome
@nd m@ny girls like him
```

# Advanced replace
```
sed  "s/\([am]\)/{\1}/g" /tmp/txtfile
This is {a} text file
h{a}s {a}n i{m}port{a}nt infor{m}{a}tion
M{a}nhDung is so h{a}ndso{m}e
{a}nd {m}{a}ny girls like hi{m}

\1 is origin text that capture by regex \([am]\)
```
