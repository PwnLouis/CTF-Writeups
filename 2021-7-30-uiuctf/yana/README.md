# UIUCTF - yana (21 solves)

> I made a note taking website. Can you get the admin's note?

**Category**: web
**Given**: 
- [bot.js](handouts/bot.js): Admin bot source code

**Requirements**: N/A
**Solution Files**: N/A
**TL;DR**: Cache exfiltration with by timing cache hits.

### Overview
I did try to tackle this challenge but I had no idea how to even start. [This writeup](https://ctf.zeyu2001.com/2021/uiuctf-2021/yana) was quite awesome! I learned about some invaluable tools for web exploitation:
- [ngrok](https://ngrok.com): Public URLs for local servers
- [webhook.site](https://webhook.site): HTTP request logger
- [crt.sh](https://crt.sh): Subdomain enumeration tool

**Flag**: uiuctf{y0u_m4y_w4nt_2_d3let3_y0ur_gh_p4g3s_s1t3_or_r1sk_0thers_d01ng_4_crtsh_lo0kup}