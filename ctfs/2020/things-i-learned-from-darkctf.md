# Things I learned from DarkCTF

## Forensics

### Wolfie's Contact

How to mount an EWF image file \(E01\) on Linux\[[link](https://www.andreafortuna.org/2018/04/11/how-to-mount-an-ewf-image-file-e01-on-linux/)\]:

```text
ewfmount IMAGE.E01 ./rawimage/
mkdir mountpoint # mount ./rawimage/ewf1 ./mountpoint -o ro,loop,show_sys_files,streams_interace=windows
```

### AW

If the file is named _"spectre"_, they may be implying that I should inspect the spectrogram 🤦‍♂️

### Free Games

The writeup I read used [autopsy](https://www.autopsy.com/) to search the file system for. I tried to figure out why `grep` didn't work for me and I realized the link I was looking for is split into two lines. To prevent this I could use a tool or look for _"PencakSilat"_ instead of _"http"_. 

### Crcket

This challenge was about fixing a png. It required knowledge of the [PNG structure](http://www.libpng.org/pub/png/spec/1.2/PNG-Chunks.html), and could use the help of [png-parser](https://github.com/Hedroed/png-parser).

## Cryptography

### Pipe Rhyme

First RSA challenge.

* [FactorDB](http://factordb.com/) - a factorization Database.
* [angr](https://github.com/angr/angr).
* [z3](https://github.com/Z3Prover/z3).

## Linux

### Linux Starter

Escape rbash restricted shell through SSH:

```text
ssh <User>@<IP-Adress> -t "bash --noprofile"
```

### Find Me

Use `lsof` to restore deleted files \[If they are still opened by a process\]\[[link](https://www.linux.com/news/bring-back-deleted-files-lsof/)\]:

```text
cp /proc/<PID>/fd/<FD> <Restored File>
```

### Secret Vault

Base85 is a thing, and it looks something like this:

```text
\0Ec5e;DffZ(EZee.Bl.9pF"AGXBPCsi+DGm>@
```

Also, I liked this syntax of while loop to crack the vault:

```text
nr=0; while true; do nr=$((nr+1)); if [[ $(./vault $nr) != *"wrong"* ]]; then ./vault $nr; echo $nr; fi; done;
```

### Time Eater

Sometimes you just have to keep enumerating... 😒

## Misc

### QuickFix

????

### P\_g\_G\_i\_P\_t

#### What can I do with PGP Fingerprint?

Grap the PGP key with:

```text
gpg --recv-key <PGP Fingerprint>
```

In this challenge, the key doesn't contain user ID so this won't work. Another way to obtain a key from a fingerprint is by using an online lookup like [this one](http://keys.gnupg.net/).

## OSINT

### Eye & Time Travel

Google lens and [Yandex](https://yandex.com/images/) are good tools for reverse image search.

## PWN

### roprop

Finally learned how to [ROP](https://codearcana.com/posts/2013/05/28/introduction-to-return-oriented-programming-rop.html#:~:text=What%20is%20ROP%3F,counter%20common%20exploit%20prevention%20strategies.&text=When%20using%20ROP%2C%20an%20attacker,other%20location%20in%20the%20program.)!

## Web

### Source

You can present very large numbers in PHP in this short manner:

```text
echo 9e9; //9000000000
```

### Dusty Notes

Fuzzing input fields might yield nice errors.

### Chain Race

#### Apache2 Interesting Default Files

* /etc/apache2/apache2.conf
* /etc/apache2/ports.conf

#### Race Condition Vulns

The idea is to force a program to handle tasks in an unintended order. Usually happens when several threads are operating on the same resources with a time gap between initialization and usage.

