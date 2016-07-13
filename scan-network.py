# Looks for ARP probe in your local network to find your dash button

from scapy.all import *

def arp_display(pkt):
  if pkt[ARP].op == 1: 
    if pkt[ARP].psrc == '0.0.0.0':
      print("New ARP probbe from " + pkt[ARP].hwsrc)

print(sniff(prn=arp_display, filter="arp", store=0, count=10))
 
