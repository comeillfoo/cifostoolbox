#!/usr/bin/python3
import matplotlib.pyplot as plt # to build graphs
from sys import stdin # to read stdin

def nlwpstater_plot( data ):
    plt.rcParams["figure.figsize"] = 16, 9
    plt.grid()
    for tid in data.keys():
        Xs = [ x for x in range( len( data[ tid ] ) ) ]
        plt.plot( Xs, data[ tid ], label=tid )
    plt.legend( loc='lower right', framealpha = 0.25 )
    plt.title( "Threads status" )
    plt.savefig( 'nlwpstater.png' )


def main():
    data = {}
    for line in stdin:
        tid, status = line.split( )
        try: 
            data[ tid ].append( status )
        except KeyError:
            data[ tid ] = [ status ]
            
    nlwpstater_plot( data )


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass