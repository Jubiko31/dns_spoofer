# >> DNS Spoofing tool <<

## What is DNS Spoofing

DNS Spoofing or poisoning is process to modify DNS server to redirect a targeted user to a malicious website under attacker control.

![image](https://user-images.githubusercontent.com/53910160/229233873-cfcf8cb1-4cf9-419f-9b29-766cb5cc7845.png)


## Requirements:
Python v3

Netfilterqueue

## Steps:
```sh
# Redirect iptables to bind queues:
$ ./ipt_spoof.sh

# Run DNS spoof:
$ python dns_spoof -a [TARGETADDRESS] -r [RDATA]

# Flush iptables to normal again:    
$ ./ipt_flush.sh 

# man
$ python dns_spoof.py --help
```

## Usage:
With DNS spoofing we can redirect target to any site we want instead of what target inputed as domain without even realising because domain does not change during attack. For example to fake login pages, fake sites, downalods, updates etc. This is very powerful attack because only thing required is to be the-man-in-the-middle. 

## DISCLAIMER:
I wrote this tool only for educational purposes. This kind of action is against law if you do not have permission. You have been warned.

@ All Rights Reserved.


## Manual:
![dns_spoof_man](https://user-images.githubusercontent.com/53910160/229232572-4bb38670-9833-4423-adcb-331a1c89f9c1.png)

## Example:
![dns_spoof](https://user-images.githubusercontent.com/53910160/229232612-63b5f07d-ef77-4ee1-93a9-a30cb3d0c13f.png)
