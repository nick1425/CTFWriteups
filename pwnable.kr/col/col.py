from pwn import *

session = ssh(host='pwnable.kr', user='col', port=2222, password='guest')
io = session.process('/bin/sh', env={"PS1":""})
io.sendline("./col {}".format('\x01' * 16 + '\xE8\x05\xD9\x1D'))
print(io.recvrepeat(1))