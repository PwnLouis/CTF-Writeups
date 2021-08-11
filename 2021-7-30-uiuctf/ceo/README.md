# UIUCTF - CEO (203 solves)

> You just wirelessly captured the handshake of the CEO of a multi-million dollar company! Use your password cracking skills to get the password! Wrap the password in the flag format. E.g: uiuctf{password}

**Category**: misc
**Given**: 
- [megacorp-01.cap](handouts/megacorp-01.cap): packet capture file of a wireless handshake

**Requirements**: [hashcat](https://hashcat.net/hashcat), [cap2hashcat], [rockyou.txt](https://downloads.skullsecurity.org/passwords/rockyou.txt.bz2), [hash-identification]
**Solution Files**: [hashes.hc22000](hashes.hc22000)
**TL;DR**: Crack WPA hash for password.

As the description explains, we need to crack the password (most likely a WPA/WPA2 password). Digging around the internet, I found guides like [this](https://securitytutorials.co.uk/how-to-capture-crack-wpa-wpa2-wireless-passwords), but the general idea is to extract the hash from the [pcap file](https://en.wikipedia.org/wiki/Pcap), then crack the hash with hashcat.

Using [cap2hashcat] (for convenience, [cap2hccapx](https://github.com/hashcat/hashcat-utils) probably works as well), we get a `.hc22000` with the hash(es). To crack the hash, we need a password list (the challenge is marked for beginners, so the password is probably simple enough). rockyou.txt is the most common one, so that's the one I used.

We also need to know the specific type of hash we are working with so that the information can be provided to hashcat. I did this by using [hash-identification], which showed that the hash was in a `WPA PBKDF2 (PMKID/EAPOL)` format.

To provide the hash format to hashcat, I ran `hashcat.exe -h`, which gave me a list of IDs corresponding to different formats. In particular, this is the ID I was looking for (also given in the file extension):

```
   2500 | WPA-EAPOL-PBKDF2                                    | Network Protocols
   2501 | WPA-EAPOL-PMK                                       | Network Protocols
  22000 | WPA-PBKDF2-PMKID+EAPOL  <-------                    | Network Protocols
  22001 | WPA-PMK-PMKID+EAPOL                                 | Network Protocols
  16800 | WPA-PMKID-PBKDF2                                    | Network Protocols
  16801 | WPA-PMKID-PMK                                       | Network Protocols
```

Now, let the cracking begin!
```
D:\Programs\hashcat> hashcat.exe -m 22000 hashes.hc22000 rockyou.txt
...
d360eb021386cc0be49373db8cb80556:e4956e459024:e2df7a554b2e:joesheer:nanotechnology
26d1570d08ed13bdc5f5cb40ca4b84c1:e4956e459024:96a3481e2f4d:joesheer:nanotechnology
```

**Flag**: uiuctf{nanotechnology}

[cap2hashcat]: https://hashcat.net/cap2hashcat
[hash-identification]: https://www.onlinehashcrack.com/hash-identification.php