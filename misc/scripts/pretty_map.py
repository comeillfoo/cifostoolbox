#!/usr/bin/python3
from sys import stdin

colours = [ '\033[0;36m', '\033[0;32m', '\033[1;36m', '\033[0;36m', '\033[1;30m', '\033[1;36m' ] 
nocolour = '\033[0m'

def pretty_line( line ):
    ps = line.split( )
    for idx in range( len( ps ) - 1 ):
        print( colours[idx], ps[idx], nocolour, end="\t", sep='' )
    lidx = len( ps ) - 1
    print( colours[lidx], ps[lidx], nocolour, end='\n', sep='' )

def main():
    for line in stdin:
        pretty_line( line )


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass