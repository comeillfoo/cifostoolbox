#!/usr/bin/python3
import sys # to get cmd options
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