# UIUCTF - back_to_basics (103 solves)

> Shoutout to those people who think that base64 is proper encryption

**Category**: crypto

**Given**: 
- [flag_enc](handouts/flag_enc) - encoded flag file
- [main.py] - script used to encode the flag file

**Requirements**: Python, [pycryptodome](https://pycryptodome.readthedocs.io/en/latest), [gmpy2](https://gmpy2.readthedocs.io/en/latest) (Windows wheels [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#gmpy))

**Solution Files**:
- [solve.py](solve.py)

Code in [main.py] (`base_n_encode`, `base_n_decode`) shows that the flag is encoded by base-n encoding multiple times for different values of n. In `encrypt`, each character in the "encryption key" is converted into a number by taking its index in the `ALPHABET` bytearray. 

Knowing that the maximum values of `n` is `len(ALPHABET) - 1`, the flag can be decoded by iterating through all possible `n` multiple times until the decoded string contains `uiuctf`.

**Flag**: uiuctf{r4DixAL}

[main.py]: handouts/main.py