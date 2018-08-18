# top
```
top
type 1 to see cpu number
type m to see memory visualization
```
## sort by memory
```
shift + m
```

## sort by cpu
```
shift + p - default
```

## save to file
```
top -b -n 1 > top_output
```

# atop
```
atop
type m to sort by memory
type c to show full commands
type a to filter active process
```

# iotop
```
sudo iotop
```

## list only processes doing I/O
```
sudo iotop -o
```

## delay between interaction
```
sudo iotop -d delay
```

## specify user
```
sudo iotop -u user
```

## specify pid
```
sudo iotop -p pid
```
