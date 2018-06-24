```
conference list
```
```
chat sip|1235|external/101300@10.22.0.62|text1|text/plain
1235 is virtual sip ext
101300 is sip ext you want to send message
10.22.0.62 is kamailio ip
```
```
originate sofia/external/101300@10.22.0.62 &conference(88888)
101300 is sip ext you want to invite
10.22.0.62 is kamailio ip
88888 is room numb
```
