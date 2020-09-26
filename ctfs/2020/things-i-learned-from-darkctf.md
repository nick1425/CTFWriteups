# Things I learned from DarkCTF

## Web

### Source

You can present very large numbers in PHP in this short manner:

```text
echo 9e9; //9000000000
```

### Dusty Notes

????

### Chain Race

#### Apache2 Default Interesting Files

* /etc/apache2/apache2.conf
* /etc/apache2/ports.conf

????

### Safe House

????

## Forensics

### Wolfie's Contact

How to mount an EWF image file \(E01\) on Linux\[[link](https://www.andreafortuna.org/2018/04/11/how-to-mount-an-ewf-image-file-e01-on-linux/)\]:

```text
ewfmount IMAGE.E01 ./rawimage/
mkdir mountpoint # mount ./rawimage/ewf1 ./mountpoint -o ro,loop,show_sys_files,streams_interace=windows
```

### AW

????

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

????

### Squids

????

### Time Eater

????

## Misc

### QuickFix

????

### Secret Of The Contract

????

### Minetest 3

????

### P\_g\_G\_i\_P\_t

????

## OSINT

### Eye

????

## PWN

### Roprop

????

