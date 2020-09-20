# mistake

## The Challenge

We all make mistakes, let's move on. \(don't take this too seriously, no fancy hacking skill is required at all\)

This task is based on real event, Thanks to dhmonkey.

hint: operator priority

ssh mistake@pwnable.kr -p2222 \(pw:guest\)

## The Solution

As the hint suggests the problem lies in the operator priority.

![](../.gitbook/assets/image%20%2841%29.png)

The file "password" opens successfully, but the file descriptor is larger than 0, so the equasion will evaluate to false \(0\). now that the file descriptor is STDIN we can provide the right input. We used "BBBBBBBBBB" and "CCCCCCCCCC".

