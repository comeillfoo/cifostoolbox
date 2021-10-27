#!/usr/bin/python3
import os # to check if process runs
import sys # to get cmd options
import time # to sleep
import subprocess as sp # to run external processes
import re # to get only useful information
import matplotlib.pyplot as plt # to build graphs


def stat( pid ):
    cmd = f"sudo netstat -sp {pid} | head -n 32 | tail -n 10"
    tcpstat_proc = sp.Popen( cmd, shell=True, stdout=sp.PIPE, stderr=sp.STDOUT )
    return tcpstat_proc.communicate( )[ 0 ]


regexs = list( map( lambda regex: re.compile( regex ), [ "([0-9]+) active connection openings",
"([0-9]+) passive connection openings",
"([0-9]+) failed connection attempts",
# "([0-9]+) connection resets received",
# "([0-9]+) connections established",
"([0-9]+) segments received",
"([0-9]+) segments sent out",
# "([0-9]+) segments retransmitted",
# "([0-9]+) bad segments received",
"([0-9]+) resets sent",
] ) )


script = lambda ripdata : [ int( re.search( regex, ripdata ).groups( 0 )[ 0 ] ) for regex in regexs ]
  

parameters = [ "Act.Conn.Op",
"Pass.Conn.Op",
"Fail.Conn.Atts",
# "Conn.Resets.Rec",
# "Conn.Established",
"Segs.Received",
"Segs.Sent.Out",
# "Segs.Retrasmitted",
# "Bad.Segs.Rec",
"Resets.Sent",
]