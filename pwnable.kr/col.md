# col

## The Challenge

Daddy told me about cool MD5 hash collision today.

I wanna do something like that too!

ssh col@pwnable.kr -p2222 \(pw:guest\)

## Solution

![](../.gitbook/assets/image%20%282%29.png)

The program expects one argument with a length of 20.

![](../.gitbook/assets/image%20%283%29.png)

* The 20 byte string input is converted to 5 integers \(4 byte int \* 5 = 20\).
*  The sum of these numbers should equal to 0x21DD09EC.

![](../.gitbook/assets/image%20%284%29.png)

Concatenate 0x01010101 four times and 0xE805D91D \[notice the input is little endianed\] to gain access.

