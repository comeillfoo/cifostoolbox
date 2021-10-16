#!/usr/bin/python3
import sys # to get cmd options
import subprocess as sp # to run external processes
from lss import lsthreads, is_running, list_threads
import re

def get_status( pid, tid ):
    cmd = f'cat /proc/{pid}/task/{tid}/status | grep "State:"'
    lsstate = sp.Popen( cmd, shell=True, stdout=sp.PIPE, stderr=sp.STDOUT )
    return lsstate.communicate( )[ 0 ]


regex = re.compile( "State:\t(\D) .*" )


# define main files snapshotting function
def report( pid, interval, count ):
    # is the main process running
    pisrun = is_running( pid )
    print( pid, ":", ( "running" if pisrun else "closed" ), file=sys.stderr )
    if pisrun:
        tids = list_threads( pid )
        for tid in tids: # count threads
            raw_state = get_status( pid, tid ).decode( "UTF-8" )
            print( tid, re.search( regex, raw_state ).groups( 0 )[ 0 ] )

    else:
        exit( 0 )