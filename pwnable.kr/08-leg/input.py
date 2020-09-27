from pwn import *

session = ssh(host='pwnable.kr', user='leg', port=2222, password='guest')
io = session.run('/bin/sh', env={"PS1":""})
io.recvrepeat(1)
io.sendline("./leg")
io.sendline("108400")
print(io.recvrepeat(1).decode())