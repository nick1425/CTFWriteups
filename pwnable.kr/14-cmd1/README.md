# 14 - cmd1



## The Challenge



Mommy! what is PATH environment in Linux?



ssh cmd1@pwnable.kr -p2222 \(pw:guest\)



## The Solution



This is a blacklisting challenge.



![](/.gitbook/assets/image%20%2843%29.png)



Our command can't contain "flag", "sh" or "tmp", and we dont have path. This will do the job:



```text

./cmd1 "/bin/cat fla*"

```



