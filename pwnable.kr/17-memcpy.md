# 17 - memcpy

## The Challenge

Are you tired of hacking? take some rest here. Just help me out with my small experiment regarding memcpy performance. after that, flag is yours.

[http://pwnable.kr/bin/memcpy.c](http://pwnable.kr/bin/memcpy.c)

ssh memcpy@pwnable.kr -p2222 \(pw:guest\)

## The Solution

The source code is pretty long, so here is the gist of it:

* We input sized in ranges between consecutive powers of 2 \[Ex. 64 - 128\].
* These sizes are `malloc`ed and two `memcpy` copycats are executed on them.
* The first is called `slow_memcpy`, it copies byte by byte. The second is called fast\_memcpy, it copies 64-byte chunks. This function actually kicks in when the malloced size is at least 64.

When we run the program with random valid input it crashes here:

![](../.gitbook/assets/image%20%2854%29.png)

[This](https://software.intel.com/sites/landingpage/IntrinsicsGuide/#expand=4056,5203,4056,5203,5669&text=_mm_stream) guide by intel implies that the address must be aligned by a 16-byte boundary when using `movntps`.  So be it.

`malloc` uses 8 bytes before the returned address for a header \[[source](https://sourceware.org/glibc/wiki/MallocInternals)\], so if we send a size that is smaller by 8 from a 16-byte alignment the address returned to us will be aligned.

```text
printf '8\n24\n56\n120\n248\n504\n1016\n2040\n4088\n8184') | nc 0 9022
```

