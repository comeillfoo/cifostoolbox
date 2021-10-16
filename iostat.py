#!/usr/bin/python3
import sys # to get cmd options
import time # to sleep
import subprocess as sp # to run external processes
from datetime import datetime # to watch the time
from lss import lsthreads, is_running, list_threads


# sudo iotop -bkp {pid} -n 1 | grep -Eo "%.*" | grep -Eo "[0-9]+\.[0-9]+"
def get_io_load( pid, count ):
    cmd = f'sudo iotop -bkp {pid} -n {count} | grep -Eo "%.*" | grep -Eo "[0-9]+\.[0-9]+"'
    sudoiotop = sp.Popen( cmd, shell=True, stdout=sp.PIPE, stderr=sp.STDOUT )
    return sudoiotop.communicate( )[ 0 ]


# define main files snapshotting function
def report( pid, interval, count ):
    # is the main process running
    pisrun = is_running( pid )

    print( pid, ":", ( "running" if pisrun else "closed" ), file=sys.stderr )
    if ( pisrun ):
        tids = list_threads( pid ) # list of threads' pid
        print( "threads:", ", ".join( list( map( lambda tid: str( tid ), tids ) ) ), file=sys.stderr )
        proc_load = list( map( lambda load: float( load ), get_io_load( pid, count ).decode( "UTF-8" ).splitlines() ) )
        if ( proc_load == [] ):
            proc_load = [ 0.0 ] * count 
        print( pid, *proc_load )
        for tid in tids:
            thread_load = list( map( lambda load: float( load ), get_io_load( tid, count ).decode( "UTF-8" ).splitlines() ) )
            if ( thread_load == [] ):
                thread_load = [ 0.0 ] * count
            print( tid, *thread_load )
    else:
        exit( 0 )