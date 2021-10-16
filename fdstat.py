#!/usr/bin/python3
import sys # to get cmd options
import time # to sleep
import subprocess as sp # to run external processes
from datetime import datetime # to watch the time
from lss import lsthreads, lsfd, is_running, list_threads


# define main files snapshotting function
def report( pid ):
    # is the main process running
    pisrun = is_running( pid )

    print( pid, ":", ( "running" if pisrun else "closed" ), file=sys.stderr )

    if pisrun:
        tids = list_threads( pid ) # list of threads' pid
        print( "threads:", ", ".join( list( map( lambda tid: str( tid ), tids ) ) ), file=sys.stderr )
        for tid in tids:
            try:
                # list of files that opened by thread with id
                fds = list( lsfd( tid ).decode( 'UTF-8' ).splitlines() )
                for fd in fds:
                    tstamp = datetime.now()
                    print( tid, fd, tstamp )

            except sp.CalledProcessError as e:
                print( "error in subprocess:", e.output.decode( "UTF-8" ), file=sys.stderr )
            except FileNotFoundError as fnfe:
                print( "File", fnfe.filename, "not found", file=sys.stderr )
    else:
        exit( 0 )