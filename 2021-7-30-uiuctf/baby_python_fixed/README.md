# UIUCTF - baby_python_fixed (45 solves)

> whoops, I made a typo on the other chal. it's probably impossible, right? Python version is 3.8.10 and flag is at /flag

**Category**: jail

**Given**: 
- [challenge.py](handouts/challenge.py): Challenge script

**Requirements**: Python

**Solution Files**: N/A

**TL;DR**: Exploit Python unicode normalization to sneak lowercase characters.

### Overview
This jail challenge requires the executed input to not match the following regex: `[a-z\s]`, which translates to *no lowercase letters or spaces*.

### Approach
Since Python is case-sensitive, not being able to use lowercase letters is a pain, and potentially impossible. However, due to [quirks in the language regarding unicode normalization](https://book.hacktricks.xyz/pentesting-web/unicode-normalization-vulnerability), we can use canonically equivalent unicode characters that bypass the regex filter, but get converted into their lowercase counterparts. These characters can come from websites like [this one](https://lingojam.com/ItalicTextGenerator).

### Payload
Coming up with a basic payload is quite simple once we know the trick. 
```
𝘱𝘳𝘪𝘯𝘵(__𝘣𝘶𝘪𝘭𝘵𝘪𝘯𝘴__.__𝘪𝘮𝘱𝘰𝘳𝘵__('𝘰𝘴').𝘴𝘺𝘴𝘵𝘦𝘮('𝘤𝘢𝘵 𝘧𝘭𝘢𝘨'))
```

The problem is `𝘰𝘴` & `𝘤𝘢𝘵 𝘧𝘭𝘢𝘨` are in strings, so they are interpreted as is since Python 3 has proper unicode support (there's also a space). To solve this, we can programatically get each lowercase character with the `chr` function:

```
𝘱𝘳𝘪𝘯𝘵(__𝘣𝘶𝘪𝘭𝘵𝘪𝘯𝘴__.__𝘪𝘮𝘱𝘰𝘳𝘵__((𝘤𝘩𝘳(111)+𝘤𝘩𝘳(115))).𝘴𝘺𝘴𝘵𝘦𝘮(𝘤𝘩𝘳(99)+𝘤𝘩𝘳(97)+𝘤𝘩𝘳(116)+𝘤𝘩𝘳(32)+𝘤𝘩𝘳(102)+𝘤𝘩𝘳(108)+𝘤𝘩𝘳(97)+𝘤𝘩𝘳(103)))
```


**Flag**: uiuctf{unicode_normalization_is_not_normal_d2f674}
