#!/usr/bin/python3
import sys
import subprocess as sp # to run external processes
import re
import os # to resolve symbolic links
from lss import lsthreads, is_running, list_threads
from pipe import select


refileflag = re.compile( ".?(.*)?<==.*flags:\t(\d+)?", re.DOTALL )


reflag = re.compile( "(.*)?: (\d+)?" )
# for flag in APPEND ASYNC CLOEXEC CREAT DIRECT DIRECTORY DSYNC EXCL LARGEFILE NOATIME NOCTTY NOFOLLOW NONBLOCK PATH SYNC TMPFILE TRUNC
# do
#   printf '%s: ' O_$flag;
#   echo O_$flag | gcc -D_GNU_SOURCE -include fcntl.h -E - | tail -n 1;
# done
fgparse = lambda flag: re.search( reflag, flag ).groups( 0 )
fcntlgs = {}


def lsflags():
    for flag in ( sp.run( "./misc/scripts/getfilesflags", check=True, stdout=sp.PIPE ).stdout.decode( "UTF-8" ).splitlines() ):
        name, value = fgparse( flag )
        fcntlgs[ name ] = int( str( value ), base=16 )


lsflags()


def lsfilesflag( tid ):
    cmd = f"tail -n +1 `sudo find /proc/{tid}/fdinfo/* 2>/dev/null`"
    lsfiles = sp.Popen( cmd, shell=True, stdout=sp.PIPE, stderr=sp.STDOUT )
    return lsfiles.communicate( )[ 0 ]


def report( pid, interval, count ):
    # is the main process running
    pisrun = is_running( pid )

    print( pid, ":", ( "running" if pisrun else "closed" ), file=sys.stderr )
    if ( pisrun ):
        tids = list_threads( pid ) # list of threads' pid
        print( "threads:", ", ".join( list( tids | select( lambda tid: str( tid ) ) ) ), file=sys.stderr )
        for tid in tids:
            rawfiles = [ rfile for rfile in lsfilesflag( tid ).decode( "UTF-8" ).split( "==>" ) if rfile != '' ]
            for rfile in rawfiles:
                # print( rfile )
                file_name, flags = re.search( refileflag, rfile ).groups( 0 )
                file_name = file_name.strip()
                flags = int( flags, base=16 )
                if ( flags & fcntlgs[ 'O_NONBLOCK' ] != 0 ):
                    print( f'{file_name} ->', os.readlink( file_name.replace( "info", "" ) ) )
    else:
        exit( 0 )
