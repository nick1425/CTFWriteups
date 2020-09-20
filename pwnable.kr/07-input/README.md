# input



## The Challenge



Mom? how can I pass my input to a computer program?



ssh input2@pwnable.kr -p2222 \(pw:guest\)



## The Solution



To solve this one we need to run the binary under very specific circumstances, divided into five categories.



### 1 - argv



![](/.gitbook/assets/image%20%2828%29.png)



To get through this stage we need to provide **input** with 99 arguments. The arguments indexed **A** \[65\] and **B** \[66\] need to equal to the values specified above.



```text

./input A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A $'\0' $' \n\r' A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A

```



### 2 - stdio



![](/.gitbook/assets/image%20%2835%29.png)



The program reads four bytes from **stdin** and the four bytes from **stderr**. To make stderr read data, bind it to stdin with 2&lt;&0 and send the buffer.



```text

printf '\x00\x0a\x00\xff\x00\x0a\x02\xff' | ./input A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A $'\0' $' \n\r' A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A 2<&0

```



### 3 - env



![](/.gitbook/assets/image%20%2833%29.png)



This section requires us to set an environment variable with unreadble name and value. **Export** does not support this, so we used **env** instead.



```text

printf '\x00\x0a\x00\xff\x00\x0a\x02\xff' | env $'\xde\xad\xbe\xef'=$'\xca\xfe\xba\xbe' ./input A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A $'\0' $' \n\r' A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A 2<&0

```



### 4- file



![](/.gitbook/assets/image%20%2832%29.png)



To clear this stage we need to execute the binary from a directory that contains a file named **\n** that contains four bytes of **\0**. Also, we need to create a symlink to the flag, so once we clear all the stages the flag will be printed.



Inside your  writable directory:



```text

printf '\x00\x00\x00\x00' > $'\n'

ln -s ~/flag flag

printf '\x00\x0a\x00\xff\x00\x0a\x02\xff' | env $'\xde\xad\xbe\xef'=$'\xca\xfe\xba\xbe' ~/input A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A $'\0' $' \n\r' A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A 2<&0

```



### 5 - network



![](/.gitbook/assets/image%20%2834%29.png)



The binary will wait for connection on the port specified on the argument indexed **C** \[67\]. If the data sent to the connection equals to **0xdeadbeef** we will pass the stage and recieve the flag :\)



The final one-liner \[after the prerequisites of stage 4\]:



```text

(sleep 1 && printf '\xde\xad\xbe\xef' | nc localhost 55555 &); printf '\x00\x0a\x00\xff\x00\x0a\x02\xff' | env $'\xde\xad\xbe\xef'=$'\xca\xfe\xba\xbe' ~/input A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A $'\0' $' \n\r' 55555 A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A 2<&0

```



