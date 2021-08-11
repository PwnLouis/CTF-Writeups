# UIUCTF - baby_python (19 solves)

> here's a warmup jail for you :) Python version is 3.8.10 and flag is at /flag <br>
Note: this chal is not actually broken, just thought it would be a funny joke

**Category**: jail
**Given**: 
- [challenge.py](handouts/challenge.py): Challenge script

**Requirements**: Python
**Solution Files**: N/A
**TL;DR**: Lowercase import, override `exit` with `code.interact`, spawning a REPL prompt.

### Overview
This jail challenge requires the executed input to not match the following regex: `[^a-z\s]`, which translates to *only lowercase letters and spaces*.

### Approach
I didn't think enough to be able to solve this challenge during the CTF, but some digging made it clear that with such a tight constraint, regular function calls won't work. The only function that is executed after `exec` is `exit`, so any approach would probably have to exploit that singular function call.

### Using the `exit` call
Python allows its built-in methods to be overridden, so the first step would be to override `exit` with some other function. However, `exit` only takes single parameter `bad`, which is a boolean. It is likely impossible that the single function can break us out of the Python jail.

One way to override a function is by assigning it to something else. This cannot be done since the regex doesn't allow `=`, which is needed for assingment. Another way would be to potentially use import aliasing, which would look like this: `from os import system as exit`. As we can see, only lowercase letters and spaces are used, so this could work provided that the function we use is "powerful" enough.

### Finding a function that works
At this point, an easy but tedious way to find a function that works would be to scan through the [Python Module Index](https://docs.python.org/3/py-modindex.html), and look for potentially helpful modules and functions. Eventually, you'll find the [`code`](https://docs.python.org/3/library/code.html#module-code) module, which seems to have functions that spawn a REPL interprter prompt. More specifically, `code.interact` seems like a VERY promising candidate, since we'll be able to execute arbitrary lines of code in the REPL prompt. Executing the payload results in a REPL prompt, in which we can simply grab the flag from the flag file.

```python
$ nc baby-python.chal.uiuc.tf 1337
from code import interact as exit
>>> import os
>>> os.system("cat flag") 
uiuctf{just_kidding_about_the_chal_being_broken_lol_11a7b8}
>>>
```

**Flag**: uiuctf{just_kidding_about_the_chal_being_broken_lol_11a7b8}
