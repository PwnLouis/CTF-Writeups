import binascii
from PIL import Image


def to_bin(number):
    return '{0:08b}'.format(number)


# Source: https://stackoverflow.com/a/40559005
def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))


emote = Image.open('handouts/flag.png')
print(emote.size)

msg = ''

i = 0
for row in range(120):
    for col in range(120):
        if i >= 1337:
            r, g, b, a = emote.getpixel((row, col))
            r_bin, g_bin, b_bin = to_bin(r), to_bin(g), to_bin(b)
            msg += r_bin[-1] + g_bin[-1] + b_bin[-1]
        i += 1

print(decode_binary_string(msg))

