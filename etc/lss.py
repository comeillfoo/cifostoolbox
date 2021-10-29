#!/usr/bin/python3
import subprocess as sp # to run external processes
import os

lsthreads = lambda pid: [ "sudo", "ls", f'/proc/{pid}/task' ]

# ls -l /proc/{pid}/fd | grep -oE '[^ ]+$' | tail -n +2
def lsfd( pid ):
    cmd = f"sudo ls -l /proc/{pid}/fd 2>/dev/null | grep -oE '[^ ]+$' | tail -n +2"
    sudols = sp.Popen( cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE )
    if ( not sudols.communicate( )[ 1 ] ):
        return sudols.communicate( )[ 0 ]
    else:
        return b''


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