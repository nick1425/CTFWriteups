# 08 - leg



## The Challenge



Daddy told me I should study arm. But I prefer to study my leg!



Download: [http://pwnable.kr/bin/leg.c](http://pwnable.kr/bin/leg.c)



Download: [http://pwnable.kr/bin/leg.asm](http://pwnable.kr/bin/leg.asm)



ssh leg@pwnable.kr -p2222 \(pw:guest\)



## The Solution



![](/.gitbook/assets/image%20%2829%29.png)



Our input needs to equal to the sum of the three key functions.



To solve this one some knowledge of ARM Assembly is required.



### Key1



![](/.gitbook/assets/image%20%2830%29.png)



The return value of **key1** will be the value of `pc` at `0x00008cdc`, which is **`0x00008ce4`**. Yes, `pc` points two commands ahead.



### key2



![](/.gitbook/assets/image%20%2831%29.png)



`r3` contains the value of `pc` at `0x00008d08`  plus 4, which is `0x00008d0c`. It is poped onto `pc` at`0x00008d0a`, but doesn't change the execution flow as it is the address of the next instruction. Later on the value of `r3` is used as the return value.



### key3



![](/.gitbook/assets/image%20%2822%29.png)



The return value here is the value of `lr`, which is the return address of the function. That be:



![](/.gitbook/assets/image%20%2827%29.png)



### Final Input



The solution is the addition of these three values in decimal representation.







