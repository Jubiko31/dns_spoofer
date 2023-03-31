#!/bin/sh

echo "[*] redirecting iptables >>"
if iptables -I OUTPUT -j NFQUEUE --queue-num 0; then
    echo "[*] redirecting iptables <<"
else
    echo "[-] task failed."
    exit
fi
if iptables -I INPUT -j NFQUEUE --queue-num 0; then
    echo "[*] successfully redirected."
else
    echo "[-] task failed. Try again or do it manually"
fi