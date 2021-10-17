#!/usr/bin/python3
import matplotlib.pyplot as plt # to build graphs
from sys import stdin # to read stdin

def pidstat_plot( data ):
    plt.rcParams["figure.figsize"] = 16, 9
    plt.grid()
    Xs = [ x for x in range( len( data ) ) ]
    plt.plot( Xs, data, label='%cpu' )
    plt.legend( loc='lower right', framealpha = 0.25 )
    plt.title( "CPU % load avg" )
    plt.savefig( 'pidstat.png' )


def main():
    data = []
    for line in stdin:
        data.append( float( line ) )
    pidstat_plot( data )


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass