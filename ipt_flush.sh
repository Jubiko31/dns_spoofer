#!/bin/bash

echo "* Flushing iptables..."
if iptables --flush; then
	echo "* done."
else
	echo "[X] something went wrong..."
fi