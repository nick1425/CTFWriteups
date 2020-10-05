# 13 - lotto



## The Challenge



Mommy! I made a lotto program for my homework. do you want to play?



ssh lotto@pwnable.kr -p2222 \(pw:guest\)



## The Solution



The code seems to work overall. It asks the user to input 6 characters \[between the ASCII values of 1 - 45\]. If the input maches the randomized value we win the lottery and get the flag. This challenge should take a long time to solve unless this faul logic:



![](/.gitbook/assets/image%20%2836%29.png)



Take a closer look. The match variable will be increased six times if one digit from our guess is contained in the lotto string. After several attempts of a single digit repeated six times this should work :\)



