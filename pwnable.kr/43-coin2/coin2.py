from pwn import *


def get_number_list(coint_count, bit):
    res = []
    for i in range(0,coint_count):
        if (i & (2**bit)) != 0:
            res.append(str(i))
    return ' '.join(res)


def solve_once():
   
    raw=shell.recvline().decode()
    coin_count = int(raw.split(' ')[0][2:])
    bits = int(math.ceil(math.log(coin_count,2)))
    huge_list = []
    for i in range(0, bits):
        l = get_number_list(coin_count, i)
        huge_list.append(l)

    shell.sendline('-'.join(huge_list))
    print("huge-list:", huge_list)
    results = shell.recvline().decode()[:-1].split('-')
    print("results:", results)
    result = 0
   
    for i in range(0, bits):
        if results[i][-1] == '9':
            result += 2**i

    print("result:", result)
    shell.sendline(str(result))
    print(shell.recvline().decode())




shell = remote('pwnable.kr',9008)
shell.recvrepeat(1)

for i in range(0,100):
    solve_once()
print(shell.recvrepeat(1).decode())