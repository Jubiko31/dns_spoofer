# >> DNS Spoofing tool <<

## Requirements:
Python v3
Netfilterqueue

## Steps:
```sh
# Redirect iptables to bind queues
$ ./ipt_spoof.sh
# Run DNS spoof againt target machine
$ python dns_spoof -a [TARGETADDRESS] -r [RDATA]
# Flush iptables to normal again       
$ ./ipt_flush.sh 

# man
$ python dns_spoof.py --help
```

## Usage:
With DNS spoofing we can redirect target to any site we want instead of what target inputed as domain without even realising because domain does not change during attack. For example to fake login pages, fake sites, downalods, updates etc. This is very powerful attack because only thing required is to be the-man-in-the-middle. 

## DISCLAIMER:
I wrote this tool only for educational purposes. This kind of action is against law if you do not have permission. You have been warned.
All Rights Reserved.

## Example: