#!/usr/bin/python3
import matplotlib.pyplot as plt # to build graphs
from sys import stdin # to read from stdin

def fdstat_plot( data ):
    plt.rcParams["figure.figsize"] = 20, 9
    plt.grid()

    for key in data.keys():
        data[ key ][ 0 ].sort()
        plt.plot( data[ key ][ 0 ], data[ key ][ 1 ], 'o', label=key )
    plt.legend( loc='lower right', framealpha = 0.25 )
    plt.title( "Files opened by threads" )
    plt.savefig( 'fdstat.png' )


def main():
    times = []
    input = []
    threads = {}
    for line in stdin:
        tid, file, tm = line.split( ' ', maxsplit = 3 )
        if ( file.startswith( 'socket:' ) ):
            continue
        input.append( line )
        threads[ tid ] = ( [], [] )
        times.append( float( tm ) )

    mintime = min( times )

    for line in input:
        tid, file, tm = line.split( ' ', maxsplit = 3 )
        threads[ tid ][ 0 ].append( float( tm ) - mintime )
        threads[ tid ][ 1 ].append( file )

    fdstat_plot( threads )

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass