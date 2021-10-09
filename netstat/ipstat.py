#!/usr/bin/python3
import os # to check if process runs
import sys # to get cmd options
import time # to sleep
import subprocess as sp # to run external processes
import re # to get only useful information
import matplotlib.pyplot as plt # to build graphs

def is_running( pid ):
    try:
        os.kill( pid, 0 )
    except OSError:
        return False
    else:
        return True

def ipstat( pid ):
    cmd = f"sudo netstat -sp `../getpid.sh {pid}` | head -n 9"
    ipstat_proc = sp.Popen( cmd, shell=True, stdout=sp.PIPE, stderr=sp.STDOUT )
    return ipstat_proc.communicate( )[ 0 ]

regexs = list( map( lambda regex: re.compile( regex ),
[ #"Forwarding: ([0-9]+)",
"([0-9]+) total packets received",
#"([0-9]+) with invalid addresses", 
#"([0-9]+) forwarded",
#"([0-9]+) incoming packets discarded",
"([0-9]+) incoming packets delivered",
#"([0-9]+) requests sent out",
#"([0-9]+) outgoing packets dropped",
] ) )

ipscript = lambda ripdata : [ int( re.search( regex, ripdata ).groups( 0 )[ 0 ] ) for regex in regexs ]


# define main files snapshotting function
def report( pid, fs, fs_keys, fs_key_size ):
    # is the main process running
    pisrun = is_running( pid )

    print( pid, ":", ( "running" if pisrun else "closed" ), file=sys.stderr )


    if pisrun:
        ripdata = ipstat( pid ).decode( "UTF-8" )
        ipdata = ipscript( ripdata )
        for idx in range( fs_key_size ):
            fs[ fs_keys[ idx ] ].append( ipdata[ idx ] )
        return fs
    else:
        exit( 0 )
    

parameters = [ # "Forwarding",
"Total.Packs.Received",
#"Packs.Inv.Addrs",
# "Forwarded",
#"Inc.Packs.Discarded",
"Inc.Packs.Delivered",
#"Req.Sent",
#"Out.Packs.Dropped",
]


def ipstat_plot( data ):
    plt.grid()
    xs = [ x for x in range( len( data[ parameters[ 0 ] ] ) ) ]
    for key in data.keys():
        plt.plot( xs, data[ key ], label=key )
    plt.legend()
    plt.savefig( 'ipstat.png', dpi=1200 )


# 0: file script path
# 1: pid: id of the observed process
# 2: interval: amount of time in milliseconds between reports
# 3: count: number of generated reports
def main( argc, argv ):
    if ( argc < 4 ):
        print( "not enough parameters passed", file=sys.stderr )
    else:
        params = argv[ 1: ]
        pid, interval, count = list( map( int, params ) )
        interval = float( interval ) / 1000
        print( f'pid={pid}', f'interval={interval}', f'count={count}', file=sys.stderr )

        fs = { param: [] for param in parameters }
        fs_keys = list( fs.keys() )
        fs_keys_size = len( fs_keys )

        # make a report count times with interval seconds
        while ( count > 0 ):
            report( pid, fs, fs_keys, fs_keys_size )
            count -= 1
            time.sleep( interval )
        ipstat_plot( fs )


if __name__ == '__main__':
    main( len( sys.argv ), sys.argv )