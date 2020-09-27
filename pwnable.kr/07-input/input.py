from pwn import *

session = ssh(host='pwnable.kr', user='input2', port=2222, password='guest')
io = session.process('/bin/bash', env={"PS1":""})

io.sendline('mkdir /tmp/nickbarak') #make dir in temp
io.sendline('cd /tmp/nickbarak') #move wd to the dir
io.sendline('rm -rf *') #clear the dir from past runs
io.sendline('ln -s ~/flag flag') #create link to the flag file in ~
io.sendline("printf '\\x00\\x00\\x00\\x000' > $'\\n'") #create file named \n for file portion

args = ['A'] * 100 #set argc = 100 for argv part
args[0] = '~/input' #set first arg to the file path
args[ord('A')] = "$'\\0'" #argv
args[ord('B')] = "$' \\n\\r'" #argv
args[ord('C')] = "55555"  #set port for network

#create temp env with the env var for the env portion, also redirect stderr to read from stdin
io.sendline("env $'\\xde\\xad\\xbe\\xef'=$'\\xca\\xfe\\xba\\xbe' {} 2<&0".format(' '.join(args)))

#send the input for stdin
io.sendline('\x00\x0a\x00\xff\x00\x0a\x02\xff')

#create a second process, use it to connect to the port and pass the needed value
nc = session.process('/bin/bash', env={"PS1":""})
nc.sendline("printf '\\xde\\xad\\xbe\\xef' | nc localhost 55555")

#print the result
print(io.recvrepeat(1).decode())
