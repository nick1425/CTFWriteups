# coin1

## The Challenge

Mommy, I wanna play a game! \(if your network response time is too slow, try nc 0 9007 inside pwnable.kr server\)

Running at: nc pwnable.kr 9007

## The Solution

This is more of a mathematical riddle than a pwn challenge. Check out our solver script.

 To find the counterfeit coin we ask to check all the coins with a specific bit lit. If the weight is not divisable by 10 the we know the counterfeit coin contains that bit. This process is repeated over and over.

