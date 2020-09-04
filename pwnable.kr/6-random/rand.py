from pwn import *

session = ssh(host='pwnable.kr', user='random', port=2222, password='guest')
io = session.process('/bin/sh', env={"PS1":""})

io.sendline("./random")
io.sendline('3039230856')
print(io.recvrepeat(1).decode())
