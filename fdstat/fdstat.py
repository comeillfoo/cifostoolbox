#!/usr/bin/python3
import os # to check if process runs
import sys # to get cmd options
import time # to sleep
import subprocess as sp # to run external processes

lsthreads = lambda pid: [ "ls", f'/proc/{pid}/task' ]
# ls -l /proc/{pid}/fd | grep -oE '[^ ]+$' | tail -n +2
def lsfd( pid ):
    cmd = f"sudo ls -l /proc/{pid}/fd | grep -oE '[^ ]+$' | tail -n +2"
    sudols = sp.Popen( cmd, shell=True, stdout=sp.PIPE, stderr=sp.STDOUT )
    return sudols.communicate( )[ 0 ]

def is_running( pid ):
    try:
        os.kill( pid, 0 )
    except OSError:
        return False
    else:
        return True

def list_threads( pid ):
    if ( is_running( pid ) ):
        return list( map( lambda tid: int( tid ),
                    sp.run( lsthreads( pid ), check=True, stdout=sp.PIPE ).stdout.decode( 'UTF-8' ).splitlines() ) )
    else:
        return []

# define main files snapshotting function
def report( pid ):
    # is the main process running
    pisrun = is_running( pid )
    print( pid, ( "is running" if pisrun else "have closed" ) )
    tids = list_threads( pid ) # list of threads' pid
    print( tids, "running threads" )
    for tid in tids:
        try:
            print( tid, "opened", list( lsfd( tid ).decode( 'UTF-8' ).splitlines() ) )
        except sp.CalledProcessError as e:
            print( e.output )
        except FileNotFoundError as fnfe:
            print( fnfe.filename )



# 0: file script path
# 1: pid: id of the observed process
# 2: interval: amount of time in seconds between reports
# 3: count: number of generated reports
def main( argc, argv ):
    if ( argc < 4 ):
        print( "not enough parameters passed", file=sys.stderr )
    else:
        params = argv[ 1: ]
        pid, interval, count = list( map( int, params ) )
        interval = float( interval )
        print( f'pid={pid}', f'interval={interval}', f'count={count}' )

        # make a report count times with interval seconds
        while ( count > 0 ):
            report( pid )
            count -= 1
            time.sleep( interval )

if __name__ == '__main__':
    main( len( sys.argv ), sys.argv )