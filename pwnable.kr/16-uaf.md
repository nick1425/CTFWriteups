# 16 - uaf

## The Challenge

Mommy, what is Use After Free bug?

ssh uaf@pwnable.kr -p2222 \(pw:guest\)

## The solution

Let's take a look at main:

![](../.gitbook/assets/image%20%2853%29.png)

It creates two Human objects and repeatedly offers us three options:

1. **use** - execute the `introduce` function of Jack and Jill.
2. **after** - Let us allocate data of our choice.
3. **free** - deletes both Jack and Jill.

We will use a quirk of the heap. If we allocate data of a size that was recently deallocated, it will probably allocate in the same place.

Also, look at the definition of the human class:

![](../.gitbook/assets/image%20%2851%29.png)

Who knew every human can give us a shell :\)

Armed with this knowledge our steps should be:

1. Deallocate Jack and Jill by selecting "free".
2. Allocate Human-sized data, but replace the address of the VTable so a call to `introduce` will call `give_shell`. Do this several times by calling "after", because Jill is the last to be deallocated.
3. Select "use" and get shell :d\)

We still have some questions unanswered before execution.

#### What is the size of a Human?

This is how CPP's new instruction looks in gdb:

![](../.gitbook/assets/image%20%2852%29.png)

this 0x18 is the size to be allocated.

#### What is the address we need to send?

The address of Man VTable is `0x401570`. `give_shell` is located right there, while the next address is the address of `introduce`. It seems the program calls the pointer located in an offset of 0x8 inside the VTable, so let's lie and say that the VTable starts `0x8` earlier. Our input file will look something like this:

![](../.gitbook/assets/image%20%2850%29.png)

Create that file and call uaf with:

```text
~/uaf 24 input.txt
```

Execute free -&gt; after \[several times\] -&gt; use to get shell.

