from pwn import *
import binascii
from itertools import cycle

def xor(a, b):
    return bytes([i^j for i,j in zip(a,b)])

def pad(text, size):
    return text*(size//len(text)) + text[:size%len(text)]

def xor_num(c_num, k_num):
    return bytearray([c ^ k for c, k in zip(c_num, cycle(k_num))])


def decrypt(ct):
    print(f'ct: {ct}')
    allthing = xor(bytearray.fromhex('ee' * len(ct)), ct)
    print(allthing)
    hexlified = binascii.hexlify(allthing).decode('ascii')
    print(hexlified)
    print('-' * 20)
    print(hexlified[:64])
    print('key ^')
    found_key = hexlified[:64]

    print('decoded:')
    print(xor_num(list(ct), list(pad(bytearray.fromhex(found_key), len(ct)))))
    decoded = binascii.hexlify(xor(ct, pad(bytearray.fromhex(found_key), len(ct))))
    print(decoded)
    parsed = binascii.unhexlify(decoded)
    print(parsed)
    print('-' * 10)

decrypt(bytearray.fromhex(input("Ciphertext: ")))
# BSNoida{how_can_you_break_THE_XOR_?!?!}

def main():
    ip = '127.0.0.1'
    conn = remote(ip, 1338)
    print(conn.recvline())
    print(conn.recvline()) 
    conn.recvuntil(b'[plaintext (hex)]>', drop=True)

    in_bytes = b'e' * 200 
    conn.send(in_bytes + b'\r\n')

    ciphertext = conn.recvline().split(b'> ')[1][:-1].decode('ascii')
    ct = bytearray.fromhex(ciphertext)

    print(f'in: {in_bytes}')
    print(f'ct: {ciphertext}')
    print('-' * 20)

    decrypt(ciphertext)

    conn.close()