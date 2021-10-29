#!/usr/bin/python3
import matplotlib.pyplot as plt # to build graphs
from sys import stdin # to read from stdin

def iostat_plot( kbreads, kbwrites ):
    Xs = [ x for x in range( len( kbreads ) ) ]
    fig = plt.figure()
    plt.rcParams["figure.figsize"] = 16, 9
    plt.grid()
    plt.title( "IO read Kb" )
    plt.plot( Xs, kbreads, label='Read Kb' )
    plt.legend( loc='lower right', framealpha = 0.25 )
    plt.savefig( 'iostat_read.png' )

    fig = plt.figure()
    plt.rcParams["figure.figsize"] = 16, 9
    plt.grid()
    plt.title( "IO write Kb" )
    plt.plot( Xs, kbwrites, label='Write Kb' )
    plt.legend( loc='lower right', framealpha = 0.25 )
    plt.savefig( 'iostat_write.png' )


def main():
    kbreads, kbwrites = [], []
    for line in stdin:
        rkb, wkb = list( map( lambda raw: float( raw ), line.split( " " ) ) )
        kbreads.append( rkb )
        kbwrites.append( wkb )
    iostat_plot( kbreads, kbwrites )


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass