import random
from Crypto.Cipher import AES


def pad_key(k):
    # pad key to 16 bytes (128bit)
    key = ""
    i = 0
    padding = "uiuctf2021uiuctf2021"
    while (16 - len(key) != len(k)):
        key = key + padding[i]
        i += 1
    key = key + k
    key = bytes(key, encoding='ascii')
    return key

# generate key
gpList = [ [13, 19], [7, 17], [3, 31], [13, 19], [17, 23], [2, 29] ]
#g, p = random.choice(gpList)
#a = random.randint(1, p)
#b = random.randint(1, p)
#k = pow(g, a * b, p)
#k = str(k)

# print("Diffie-Hellman key exchange outputs")
# print("Public key: ", g, p)
# print("Jotaro sends: ", aNum)
# print("Dio sends: ", bNum)
# print()

def crack():
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
    return None
print(f'Flag: {crack()}')
