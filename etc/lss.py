#!/usr/bin/python3
import subprocess as sp # to run external processes

lsthreads = lambda pid: [ "ls", f'/proc/{pid}/task' ]

# ls -l /proc/{pid}/fd | grep -oE '[^ ]+$' | tail -n +2
def lsfd( pid ):
    cmd = f"sudo ls -l /proc/{pid}/fd | grep -oE '[^ ]+$' | tail -n +2"
    sudols = sp.Popen( cmd, shell=True, stdout=sp.PIPE, stderr=sp.STDOUT )
    return sudols.communicate( )[ 0 ]