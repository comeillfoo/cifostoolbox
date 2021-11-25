#!/usr/bin/python3
import sys # to get cmd options
import time # to sleep
import subprocess as sp # to run external processes
from datetime import datetime # to watch the time
from lss import lsthreads, is_running, list_threads
import re
from pipe import select


# sudo iotop -bkp {pid} -n 1 | grep -Eo "%.*" | grep -Eo "[0-9]+\.[0-9]+" - deprecated
# sudo cat /proc/{pid}/io | grep -E "rchar|wchar"
def get_io_load( pid ):
    cmd = f'sudo cat /proc/{pid}/io | grep -E "read_bytes|^write_bytes"'
    sudoio = sp.Popen( cmd, shell=True, stdout=sp.PIPE, stderr=sp.STDOUT )
    return sudoio.communicate( )[ 0 ]


rechar = re.compile( ": ([0-9]+)?" )


# define main files snapshotting function
def report( pid, interval, count ):
    # is the main process running
    pisrun = is_running( pid )

    print( pid, ":", ( "running" if pisrun else "closed" ), file=sys.stderr )
    if ( pisrun ):
        tids = list_threads( pid ) # list of threads' pid
        print( "threads:", ", ".join( list( tids | select( lambda tid: str( tid ) ) ) ), file=sys.stderr )
        io_loads = get_io_load( pid ).decode( "UTF-8" ).splitlines()
        read_bytes, write_bytes = list( io_loads | select( lambda raw: int( re.search( rechar, raw ).groups( 0 )[ 0 ] ) / 1024 ) )
        print( read_bytes, write_bytes )
        # for tid in tids:
            # tid_io_loads = get_io_load( tid, count ).decode( "UTF-8" ).splitlines()
            # thread_load = list( select( tid_io_loads | lambda load: float( load ) ) )
            # if ( thread_load == [] ):
            #     thread_load = [ 0.0 ] * count
            # print( tid, *thread_load )
            
    else:
        exit( 0 )