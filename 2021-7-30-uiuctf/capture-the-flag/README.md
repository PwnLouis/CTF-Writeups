# UIUCTF - capture the :flag: (24 solves)

> It's always in the place you least expect

**Category**: forensics

**Given**: 
- N/A

**Requirements**: Python, [pillow](https://pillow.readthedocs.io), [exiftool](https://exiftool.org)

**Solution Files**: [solve.py](solve.py)

In this case, no files were given, so the file needs to be found first. Thankfully, the title gives it away. :emote_name: is Discord syntax for an emote, so I downloaded the :flag: emote from the competition server.

As this was my first time dealing with images in a CTF, I researched online and found that in these types of [image steganography](https://en.wikipedia.org/wiki/Steganography) challenges, the first thing I should do is run `exiftool` to check the image metadata. The most interesting part of the `exiftool` output was this:

```
Description                     : LSBs(Pixels[1337:])
```

Clearly this was a hint of some sort. `[1337:]` obviously meant start from the 1337th pixel onward, but what does LSB mean? Searching up "LSB image steganography" showed that LSB (least significant bit) was a way to hide data in an image by storing information in the smallest bit. Essentially, given a pixel value (R, G, B) where each channel is 2 bytes (8 bits), the smallest bit of each channel value is a bit in the original message.

Knowing how the flag was hidden in the emote, the rest can be scripted quite easily. The script iterates through every pixel, waits till the 1337th pixel, the starts concatenating the LSB into a result string. The result is then converted into a human-readable ASCII string. (The code isn't efficient but whatever :P)

```python
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
```

**Flag**: uiuctf{d!sc0rd_fl4g_h0w_b0ut_d4t}