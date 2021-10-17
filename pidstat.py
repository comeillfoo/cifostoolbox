#!/usr/bin/bash
import sys # for stderr
from lss import is_running
import subprocess as sp

def get_cpu_load( pid ):
    cmd = f'sudo ps -p {pid} -o %cpu | grep -Eo "[0-9]+\.?[0-9]+"'
    sudoiotop = sp.Popen( cmd, shell=True, stdout=sp.PIPE, stderr=sp.STDOUT )
    return sudoiotop.communicate( )[ 0 ]

def report( pid, interval, count ):
    pisrun = is_running( pid )

    print( pid, ":", ( "running" if pisrun else "closed" ), file=sys.stderr )

    if ( pisrun ):
        print( float( get_cpu_load( pid ).decode( "UTF-8" ) ) )
    else:
        exit( 0 )