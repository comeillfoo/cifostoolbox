#!/usr/bin/python3
import os # to check if process runs
import sys # to get cmd options
import time # to sleep
import subprocess as sp # to run external processes
from lss import lsthreads, is_running, list_threads
import re

def get_status( pid, tid ):
    cmd = f'cat /proc/{pid}/task/{tid}/status | grep "State:"'
    lsstate = sp.Popen( cmd, shell=True, stdout=sp.PIPE, stderr=sp.STDOUT )
    return lsstate.communicate( )[ 0 ]


regex = re.compile( "State:\t(\D) .*" )


# define main files snapshotting function
def report( pid ):
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



# 0: file script path
# 1: pid: id of the observed process
# 2: interval: amount of time in milliseconds between reports
# 3: count: number of generated reports
def main( argc, argv ):
    if ( argc < 4 ):
        print( "not enough parameters passed", file=sys.stderr )
    else:
        params = argv[ 1: ]
        pid, interval, count = list( map( int, params ) )
        interval = float( interval ) / 1000
        print( f'pid={pid}', f'interval={interval}', f'count={count}', file=sys.stderr )

        # make a report count times with interval seconds
        while ( count > 0 ):
            report( pid )
            count -= 1
            time.sleep( interval )

if __name__ == '__main__':
    main( len( sys.argv ), sys.argv )