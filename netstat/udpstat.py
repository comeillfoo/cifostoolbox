#!/usr/bin/python3
import os # to check if process runs
import sys # to get cmd options
import time # to sleep
import subprocess as sp # to run external processes
import re # to get only useful information
import matplotlib.pyplot as plt # to build graphs


def stat( pid ):
    cmd = f"sudo netstat -sp {pid} | head -n 39 | tail -n 6"
    udpstat_proc = sp.Popen( cmd, shell=True, stdout=sp.PIPE, stderr=sp.STDOUT )
    return udpstat_proc.communicate( )[ 0 ]


regexs = list( map( lambda regex: re.compile( regex ), [ "([0-9]+) packets received",
# "([0-9]+) packets to unknown port received",
# "([0-9]+) packet receive errors",
"([0-9]+) packets sent",
# "([0-9]+) receive buffer errors",
# "([0-9]+) send buffer errors",
] ) )


script = lambda ripdata : [ int( re.search( regex, ripdata ).groups( 0 )[ 0 ] ) for regex in regexs ]


parameters = [ "Packs.Rec",
# "Packs.Unk.Port.Rec",
# "Packs.Rec.Errs",
"Packs.Sent",
# "Rec.Buff.Errs",
# "Send.Buff.Errs",
]