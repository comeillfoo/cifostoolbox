#!/usr/bin/python3
import matplotlib.pyplot as plt # to build graphs
from sys import stdin # to read from stdin

def fdstat_plot( data ):
    plt.rcParams["figure.figsize"] = 16, 9
    plt.grid()

    for key in data.keys():
        data[ key ][ 0 ].sort()
        plt.plot( data[ key ][ 0 ], data[ key ][ 1 ], label=key )
    plt.legend( loc='lower right', framealpha = 0.25 )
    plt.title( "Files opened by threads" )
    plt.savefig( 'fdstat.png' )


def main():
    files = set()
    times = []
    input = []
    threads = {}
    for line in stdin:
        input.append( line )
        tid, file, tm = line.split( " " )
        threads[ tid ] = ( [], [] )
        files.add( file )
        times.append( float( tm ) )

    for line in input:
        tid, file, tm = line.split( " " )
        threads[ tid ][ 0 ].append( float( tm ) )
        threads[ tid ][ 1 ].append( file )

    fdstat_plot( threads )

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass