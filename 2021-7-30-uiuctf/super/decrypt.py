import binascii
from itertools import cycle

with open('handouts/SUPERHOT', 'rb') as f:
    data = f.read()

#data_ascii = data.decode('hex')
#data_numbers = [ord(ch) for ch in data_ascii]
data_numbers = list(data)

"""
The code here was also part of the article I found, about using
character frequencies to deduce the XOR cipher key. However, for
this challenge, the key was quite obvious.
"""
def shift(data, offset):
    return data[offset:] + data[:offset]

def count_same(a, b):
    count = 0
    for x, y in zip(a, b):
        if x == y:
            count += 1
    return count

def save_freqs():
    print ('key lengths')
    lines = []
    for key_len in range(1, 33): # try multiple key lengths
        freq = count_same(data_numbers, shift(data_numbers, key_len))

        lines.append('{0:< 3d} | {1:3d} |\n'.format(key_len, freq))
        print(key_len)
        # ^ this line does fancy formatting that outputs key_len and then freq and
        # then a bar graph

    with open('freq.txt', 'w') as f:
        f.writelines(lines)
    print('done')
"""
End of unused code
"""

def decrypt(c_num, k_num):
    return bytearray([c ^ k for c, k in zip(c_num, cycle(k_num))])

def decode():
    key = b'SUPERHOT'
    key_numbers = list(key)
    print(key_numbers)

    with open('handouts/decrypted.bin', 'wb') as f:
        f.write(decrypt(data_numbers, key_numbers))

    print('done')

decode()