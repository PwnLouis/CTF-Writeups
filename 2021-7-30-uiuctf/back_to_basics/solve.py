from Crypto.Util.number import long_to_bytes, bytes_to_long
from gmpy2 import mpz, to_binary
#from secret import flag, key

ALPHABET = bytearray(b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ#")

def base_n_encode(bytes_in, base):
    return mpz(bytes_to_long(bytes_in)).digits(base).upper().encode()

def base_n_decode(bytes_in, base):
    res = mpz(bytes_in, base=base)
    bytes_out = to_binary(res)[:1:-1]
    return bytes_out

def encrypt(bytes_in, key):
    out = bytes_in
    for i in key:
        print(i)
        out = base_n_encode(out, ALPHABET.index(i))
    return out

def decrypt(bytes_in, key):
    out = bytes_in
    for i in key:
        out = base_n_decode(out, ALPHABET.index(i))
    return out

"""
flag_enc = encrypt(flag, key)
f = open("flag_enc", "wb")
f.write(flag_enc)
f.close()
"""

bases = list(range(0, len(ALPHABET)))
bases.remove(1)
bases.remove(2)
bases = tuple(bases)

def crack():
    with open('handouts/flag_enc', 'rb') as f:
        encrypted_flag = f.read()
        while True:
            for base in bases:
                try:
                    test_decrypt = base_n_decode(encrypted_flag, base)
                except ValueError:
                    continue
                try:
                    unwrapped = test_decrypt.decode('ascii')
                    if 'uiuctf' in unwrapped:
                        print(f'Found flag: {unwrapped}')
                        return
                except UnicodeDecodeError:
                    unwrapped = None
                if unwrapped is not None:
                    print(f'Base {base}')
                    encrypted_flag = test_decrypt
                    break

crack()