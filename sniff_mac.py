#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 15:50:08 2019

@author: root
"""
import sys
import scapy.all as sp

#checking for a MAC address
if len(sys.argv) == 2:
    #assigning the MAC address
    MAC = sys.argv[1]
    #definition of the handler
    def handler(packet):
        #here we make sure that it's a probe request (Management, subtype 4)
        if packet.type == 0 and packet.subtype == 4:
            #here we make sure the mac address is the one that we care for (adr2 is the source adress for those packets)
            if MAC == packet.addr2:
                #we print the packet if it the MAC address fits
                packet.show()
      
    #we start sniffing    
    sp.sniff(iface='wlan0mon', prn=handler)
    
    
else:
    #We send an error message in case no argument is given
    print("No mac address given")