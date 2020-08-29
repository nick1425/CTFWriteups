# passcode

## The Challenge

Mommy told me to make a passcode based login system. My initial C code was compiled without any error! Well, there was some compiler warning, but who cares about that?

ssh passcode@pwnable.kr -p2222 \(pw:guest\)

## Examining the Code

The main function calls **welcome** and **login** directly after

![](../.gitbook/assets/image%20%2815%29.png)

#### Welcome

![](../.gitbook/assets/image%20%289%29.png)

It receives a 100 character string, prints it, and then exits. This can not be overflown but may be used later.

**Login**

![](../.gitbook/assets/image%20%2817%29.png)

It seems we need to make passcode1 and 2 equal to 338150 and 13371337, but proper examination shows that we can't write input into these variables because scanf is misused! Both variables are missing **&** at scanf call, and so we will change the variable pointers, not value.

## Executing the Binary

 **First execution - passcode1 is a number**

![](../.gitbook/assets/image%20%2814%29.png)

**Second execution - passcode1 is a string**

![](../.gitbook/assets/image%20%2816%29.png)

It seems the program is not interacting properly with regular input. What's going on?

Let's debug this thing.

## Debugging

We'll examine the stack at the beginning of **login** after inputting the longest allowed input, all made of 'a'.

![](../.gitbook/assets/image%20%2811%29.png)

Some of the input made its way here. Does this help us? Look closely

![](../.gitbook/assets/image%20%2813%29.png)

This is the location of passcode1. What do we find there?

![](../.gitbook/assets/image%20%2810%29.png)

The last four bytes of our input! So, we can control the value of passcode1. What can be done with it?

If you recall the examination of the code, the value requested from the user will be written to the location pointed by passcode1. Where should we make it point?

## The GOT Table

_**TODO**_

![](../.gitbook/assets/image%20%2812%29.png)

```text
r < <(python3 -c "import sys; sys.stdout.buffer.write(b'\x41' * 96 + b'\x04\xa0\x04\x08\n' + b'134514135')")
```

