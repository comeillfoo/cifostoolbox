#!/usr/bin/python3
import subprocess as sp # to run external processes
import os

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
        return list( filter( lambda tid: tid != pid, list( map( lambda tid: int( tid ),
                    sp.run( lsthreads( pid ), check=True, stdout=sp.PIPE ).stdout.decode( 'UTF-8' ).splitlines() ) ) ) )
    else:
        return []