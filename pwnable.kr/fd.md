# fd

## The Challenge

Mommy! what is a file descriptor in Linux?

ssh fd@pwnable.kr -p2222 \(pw:guest\)

## The Solution

![](../.gitbook/assets/image%20%281%29.png)

1. argv\[1\] should be equal to 0x1234 so the file descriptor will be STDIN.
2. Type LETMEWIN and here you go.

