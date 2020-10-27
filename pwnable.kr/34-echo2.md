# 34 - echo2

## The Challenge

Pwn this echo service.

download : [http://pwnable.kr/bin/echo2](http://pwnable.kr/bin/echo2)

Running at : nc pwnable.kr 9011

## The Solution

This solution will take a different approach from other writeups.

This binary is the same as echo1 with one key difference, `bof` is disabled, but `fsb` \[Format Strings Bug\] and `uaf` \[Use After Free\] are enabled.

With `fsb` we can write to some sections in memory or leak data.

On my first approach I wanted to use `fsb` to overwrite data. I abandoned it because of some issue with the null terminator \[I forgot what it was ¯\\_\(ツ\)\_/¯\].

`uaf` allocates 32 bytes, writes user input \[No Overflow\] and frees it. Why is it called `uaf`?

I noticed strange things happen if I choose to exit and then decline. A look at the code shows that even if I decline, `name` is freed. Now if we use `uaf` our input will be written where our name was.

![cleanup function](../.gitbook/assets/image%20%2866%29.png)

After an overflow of 24 characters we can overwrite the address of `greetings`, a function that is called at the start of `uaf` using a register \[for position independent code\]. Using the stack base leak we can redirect the execution to the input, which will contain shellcode :\)

There were some differences between the local and remote binaries:

* To achieve local heap leak use %3$x, for remote leak - %x
* The offset from the base was different on the remote

To overcome the second obstacle I bruteforced the offset until I obtained shell. 

