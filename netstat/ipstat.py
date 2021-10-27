#!/usr/bin/python3
import os # to check if process runs
import sys # to get cmd options
import time # to sleep
import subprocess as sp # to run external processes
import re # to get only useful information
import matplotlib.pyplot as plt # to build graphs


def stat( pid ):
    cmd = f"sudo netstat -sp {pid} | head -n 9"
    ipstat_proc = sp.Popen( cmd, shell=True, stdout=sp.PIPE, stderr=sp.STDOUT )
    return ipstat_proc.communicate( )[ 0 ]


regexs = list( map( lambda regex: re.compile( regex ),
[ # "Forwarding: ([0-9]+)",
"([0-9]+) total packets received",
# "([0-9]+) with invalid addresses", 
# "([0-9]+) forwarded",
# "([0-9]+) incoming packets discarded",
"([0-9]+) incoming packets delivered",
"([0-9]+) requests sent out",
# "([0-9]+) outgoing packets dropped",
] ) )


script = lambda ripdata : [ int( re.search( regex, ripdata ).groups( 0 )[ 0 ] ) for regex in regexs ]


parameters = [ # "Forwarding",
"Total.Packs.Received",
# "Packs.Inv.Addrs",
# "Forwarded",
# "Inc.Packs.Discarded",
"Inc.Packs.Delivered",
"Req.Sent",
# "Out.Packs.Dropped",
]