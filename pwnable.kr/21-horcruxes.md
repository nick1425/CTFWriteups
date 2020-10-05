# 21 - horcruxes

## The Challenge

Voldemort concealed his splitted soul inside 7 horcruxes. Find all horcruxes, and ROP it!

author: jiwon choi

ssh horcruxes@pwnable.kr -p2222 \(pw:guest\)

## The Solution

Lets Examine the program first.

![](../.gitbook/assets/image%20%2847%29.png)

It asks us to select a number from the menu and then how much XP did we earn. Not very informative. We copied the binary to our machine and disassembled it. This is main:

![](../.gitbook/assets/image%20%2848%29.png)

1. An alarm is set to throw us out after 60 seconds
2. The message about Voldemort is printed
3. `init_ABCDEFG` is called
4. Some security rules are set \[probably to prevent us from corrupting the machine once we achieve code execution\]
5. `ropme` is called

Let's take a look at `init_ABCDEFG`:

![](../.gitbook/assets/image%20%2845%29.png)

Seven integers named 'a' to 'g' are set to a random int. Their sum is saved in 'sum'. These variables have a global scope. Let's take a look at `ropme`:

![](../.gitbook/assets/image%20%2846%29.png)

The functions 'A' - 'G' print the values of the variables mentioned above. The EXP input uses `gets` which is great news, this is where we're going to ROP.

But wait, can't we just redirect the function to print the flag?

![](../.gitbook/assets/image%20%2849%29.png)

All of the addresses in `ropme` contain `0a`. Once `puts` receives  `\n` it halts, which means we can't jump to any position within `ropme`.

We created a ROP chain that jumps from `A` to `G` one after the other. It contains:

1. 120 character buffer that overrides the stack up to `ebp` \[included\].
2. The addresses of all of the functions `A` to `G`. Finding the addresses is easy with a disassembler. They are concatenated to each other as none of these functions require parameters.
3. The address where `ropme` is called \[since we can't resume execution within ropme\].

Now we can obtain `a` to `g` and calculate their sum \[with modulus in case the sum surpasses MAX or MIN int\].

To get a better understanding check out our [script](https://github.com/nickbhe/CTFWriteups/blob/master/pwnable.kr/21-horcruxes/horcruxes.py).

