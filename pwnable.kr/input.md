# input

## The Challenge

Mom? how can I pass my input to a computer program?

ssh input2@pwnable.kr -p2222 \(pw:guest\)

## The Solution

To solve this one we need to run the binary under very specific circumstances, divided into five categories.

### 1 - argv

![](../.gitbook/assets/image%20%2828%29.png)

To get through this stage we need to provide **input** with 99 arguments. The arguments indexed **A** \[65\] and **B** \[66\] need to equal to the values specified above.

```text
./input A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A $'\0' $' \n\r' A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A
```

### 2 - 

