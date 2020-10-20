""" 
challenge was fairly simple, but an opportunity to learn some scapy - you are provided with
a pcap file, opening in wireshark you are presented with some icmp traffic. there is a single
outgoing packet with the string 'Send the flag!' in the packet data.

the first response packet reveals a jpg file header (JFIF magic btyes), the script below carves
out the data (p.load) filtering out the first packet by IP and then stitches it all together into
a file 'flag.jpg' in which the flag can be viewed. attempts to open it using eog if available on
linux...
"""

from scapy.all import *
from os import system

with open('flag.jpg', 'wb') as f:
    f.write(b''.join([p.load for p in [p for p in rdpcap('error_reporting.pcap') if p['IP'].src == '192.168.10.113']]))
    
system('eog flag.jpg')

