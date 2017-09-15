# ponpontools - CTF toolkit (pwntools extension) 

[![Docs](https://readthedocs.org/projects/pwntools/badge/?version=stable)](https://docs.pwntools.com/)
[![Twitter](https://twitter.com/no1zy_sec)](https://twitter.com/no1zy\_sec)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](http://choosealicense.com/licenses/mit/)

Pwntools is a CTF framework and exploit development library. Written in Python, it is designed for rapid prototyping and development, and intended to make exploit writing as simple as possible.

```python
from pwn import *
context(arch = 'i386', os = 'linux')

r = remote('exploitme.example.com', 31337)
# EXPLOIT CODE GOES HERE
r.send(asm(shellcraft.sh()))
r.interactive()
```

# Documentation

Our documentation is available at [docs.pwntools.com](https://docs.pwntools.com/)

## commandline tools

1. generate an exploit template
generate an exploit.py and a cmd(gdb script)
```sh
xready --host [remote host] --port [remote port] --arch [architecture] --libc [libc file] [binary file]
```

2. Socat wrapper for local exploits
The specified executable file listens on 444 ports
```sh
sock [binary file]
```

To get you started, we've provided some example solutions for past CTF challenges in our [write-ups repository](https://github.com/No1zy/ctf/tree/master/writeups).

# Installation

Pwntools is best supported on 64-bit Ubuntu LTE releases (12.04, 14.04, and 16.04).  Most functionality should work on any Posix-like distribution (Debian, Arch, FreeBSD, OSX, etc.).  Python 2.7 is required.

Most of the functionality of pwntools is self-contained and Python-only.  You should be able to get running quickly with

```sh
apt-get update
apt-get install python2.7 python-pip python-dev git libssl-dev libffi-dev build-essential
pip install https://github.com/No1zy/ponpontools
```

# Contact
If you have any questions not worthy of a [bug report](https://github.com/No1zy/ponpontools/issues), feel free to ping us
Twitter [here](https://github.com/No1zy/ponpontools) to connect.
