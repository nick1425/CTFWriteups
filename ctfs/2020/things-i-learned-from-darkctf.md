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

????

### Crcket

????

## Cryptography

### Pipe Rhyme

????

### Duplicacy Within

????

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

????

## Misc

### QuickFix

????

### Minetest 3

????

### P\_g\_G\_i\_P\_t

????

## OSINT

### Eye & Time Travel

Google lens and [Yandex](https://yandex.com/images/) are good tools for reverse image search.

## PWN

### Roprop

????

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

### Safe House

????

