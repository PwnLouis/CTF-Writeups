# UIUCTF - pwnies_please (16 solves)

> Disguise these pwnies to get the flag!

**Category**: misc
**Given**: 
- [web.py](handouts/web.py): The backend code
- [pwny_cifar_eps_0.pth](handouts/pwny_cifar_eps_0.pth): ML model

**Requirements**: Python, flask, sqlalchemy, PyTorch, pillow, ImageHash, simplekv, numpy, werkzeug
**Solution Files**: N/A
**TL;DR**: Use model gradient to increase loss till an acceptable level.

### Overview
I did not solve or attempt this challenge, but [this writeup](https://ctf.zeyu2001.com/2021/uiuctf-2021/pwnies_please) made me realize that it was actually quite doable, given enough effort. Understanding gradient descent is enough to be able to invert the problem and intentionally sabotage the model's inputs.

**Flag**: uiuctf{th4nks_f0r_th3_pwni3s}