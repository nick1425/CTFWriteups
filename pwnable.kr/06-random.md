# 06 - random

## The Challenge

Daddy, teach me how to use random value in programming!

ssh random@pwnable.kr -p2222 \(pw:guest\)

## The Solution

![](../.gitbook/assets/image%20%2823%29.png)

Whats off here? This is not how you use rand\(\)! [This](https://stackoverflow.com/questions/1108780/why-do-i-always-get-the-same-sequence-of-random-numbers-with-rand) is how you use rand.

As a result of that, the same number will be generated over and over again. Here it is:

![](../.gitbook/assets/image%20%2825%29.png)

After XORing with 0xdeadbeef and translating to a number:

 

![](../.gitbook/assets/image%20%2826%29.png)

