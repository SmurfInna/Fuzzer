#!/usr/bin/python

from scapy.all import *
send(I{(dst="<ip>")/UDP()/fuzz(DNS()),loop=1)

