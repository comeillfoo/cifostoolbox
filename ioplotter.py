#!/usr/bin/python3
import matplotlib.pyplot as plt # to build graphs
from sys import stdin # to read from stdin

def iostat_plot( data ):
    plt.rcParams["figure.figsize"] = 16, 9
    plt.grid()
    for key in data.keys():
        Xs = [ x for x in range( len( data[ key ] ) ) ]
        plt.plot( Xs, data[ key ], label=key )
    plt.legend( loc='lower right', framealpha = 0.25 )
    plt.title( "IO %% average per thread" )
    plt.savefig( 'iostat.png' )


def main():
    threads_load = {}
    for thread in stdin:
        params = thread.split( " " )
        threads_load[ params[ 0 ] ] = list( map( lambda load: float( load ), params[ 1: ] ) )
    iostat_plot( threads_load )


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass