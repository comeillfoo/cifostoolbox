#!/usr/bin/python3
import matplotlib.pyplot as plt # to build graphs
from sys import stdin # to read stdin

def nlwpstat_plot( data ):
    plt.rcParams["figure.figsize"] = 16, 9
    plt.grid()
    Xs = [ x for x in range( len( data ) ) ]
    plt.plot( Xs, data, label='Threads' )
    plt.legend( loc='lower right', framealpha = 0.25 )
    plt.title( "Threads Count" )
    plt.savefig( 'nlwpstat.png' )


def main():
    data = []
    for line in stdin:
        data.append( int( line ) )
    nlwpstat_plot( data )


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass