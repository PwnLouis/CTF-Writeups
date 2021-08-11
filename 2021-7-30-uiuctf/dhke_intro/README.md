# UIUCTF - dhke_intro (166 solves)

> Small numbers are bad in cryptography. This is why.

**Category**: crypto

**Given**: 
- [dhkectf_intro.py](handouts/dhkectf_intro.py): full DHKE script
- [output.txt](handouts/output.txt): encrypted flag

**Requirements**: Python, [pycryptodome](https://pycryptodome.readthedocs.io/en/latest)

**Solution Files**: [solve.py](solve.py)

**TL;DR**: Bruteforce all possible combination of private keys to decrypt the message.

DHKE, which stands for [Diffie-Hellman key exchange](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange#Cryptographic_explanation), is a widely used protocol for securely exchanging keys over a public channel. Wikipedia's explanation is pretty good for understanding what happens. Basically, two sides generate their own private key. Once we get the private key, messages can be decrypted into plaintext very easily. Typically, it is unfeasable to brute force the private keys, but in the provided encryption script, we can see that the possible values of `a` & `b` are not that large:

```python
# generate key
gpList = [ [13, 19], [7, 17], [3, 31], [13, 19], [17, 23], [2, 29] ]
g, p = random.choice(gpList)
a = random.randint(1, p)
b = random.randint(1, p)
```

Hence, a brute force search on `a` & `b` (which is not necessary, only one of the private keys is needed) can be done very easily:

```python
iv = bytes("kono DIO daaaaaa", encoding = 'ascii')
ciphertext = 'b31699d587f7daf8f6b23b30cfee0edca5d6a3594cd53e1646b9e72de6fc44fe7ad40f0ea6'
ciperbytes = bytes(bytearray.fromhex(ciphertext))

for pair in gpList:
    g, p = pair
    for a in range(1, g):
        for b in range(1, p):
            k = str(pow(g, a * b, p))

            cipher = AES.new(pad_key(k), AES.MODE_CFB, iv)
            plaintext = cipher.decrypt(ciperbytes)
            decoded = plaintext.decode('utf-8', 'backslashreplace')
            if 'uiuctf' in decoded:
                print(f"The message is authentic: {decoded}")
                return decoded
```

**Flag**: uiuctf{omae_ha_mou_shindeiru_b9e5f9}
