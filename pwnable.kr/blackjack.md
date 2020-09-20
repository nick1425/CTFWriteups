# blackjack

## The Challenge

Hey! check out this C implementation of blackjack game! I found it online

* [http://cboard.cprogramming.com/c-programming/114023-simple-blackjack-program.html](http://cboard.cprogramming.com/c-programming/114023-simple-blackjack-program.html)

I like to give my flags to millionares. how much money you got?

Running at: nc pwnable.kr 9009

## The Solution

We need to own more than a million dollars. After some interaction with the game, it is obvious we can't profit that much in legitimate ways.

Here is the betting function:

![](../.gitbook/assets/image%20%2840%29.png)

The program is caring enough to not let us bet more than what we have, but what if we bet with a negative amount?

Most of the games we will lose, and when we lose our bet is subtracted from our total amount: 

![](../.gitbook/assets/image%20%2839%29.png)

So, just bet with a negative amount greater than a million, and grab that flag.

