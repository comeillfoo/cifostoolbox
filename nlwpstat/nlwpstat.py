#!/usr/bin/python3
import os # to check if process runs
import sys # to get cmd options
import time # to sleep
import subprocess as sp # to run external processes
from datetime import datetime # to watch the time
from lss import lsthreads, is_running, list_threads


# define main files snapshotting function
def report( pid ):
    # is the main process running
    pisrun = is_running( pid )

    print( pid, ":", ( "running" if pisrun else "closed" ), file=sys.stderr )

    if pisrun:
        print( datetime.now(), len( list_threads( pid ) ) ) # count threads
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