# flag



## The Challenge



Papa brought me a packed present! let's open it.



Download: [http://pwnable.kr/bin/flag](http://pwnable.kr/bin/flag)



This is a reversing task. all you need is binary



## The Solution



### Unpacking



running the binary outputs this:



![](/.gitbook/assets/image%20%2818%29.png)



NO input, just this. Opening a debugger won't help, **this binary is packed**. It is hinted in the challenge description and confirmed if one tries to debug this monstrosity.



To find how the binary was packed run the strings command, and look for strings longer than 30 characters \[this number was chosen arbitrary, not too short and not too long\].



![](/.gitbook/assets/image%20%2820%29.png)



To examine the file we need to **unpack** it using UPX.



### Debugging



The main function looks like this



![](/.gitbook/assets/image%20%2819%29.png)



They told the truth, It seems the flag is really copied to a malloced location.



We'll set a breakpoint after the copying and examine the memory marked as "flag".



![](/.gitbook/assets/image%20%2821%29.png)







