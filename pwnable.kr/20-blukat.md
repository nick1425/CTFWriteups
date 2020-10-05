# 20 - blukat

## The Challenge

Sometimes, pwnable is strange... hint: if this challenge is hard, you are a skilled player.

ssh blukat@pwnable.kr -p2222 \(pw: guest\)

## The Solution

This challenge is about paying attention and questioning reality itself.

At first glance everything is as usual:

![](../.gitbook/assets/image%20%2861%29.png)

Only members of `blukat_pwn` can access the password which we need to get the flag. As we started analyzing the challenge we had some opportunities to figure out something was wrong. For example:

* How did we just copy the password file to my local machine?
* Why `fgets` stores in memory _"cat: password: Permission denied"_ ?

Take a close look at blukat's group permissions:

![](../.gitbook/assets/image%20%2858%29.png)

We are part of the `blukat_pwn` group, and that permission denied string is the password!

![](../.gitbook/assets/image%20%2860%29.png)

Use this to grab the flag and get this over with.

