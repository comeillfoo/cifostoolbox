#!/usr/bin/python3
import time
import sys

# 0: file script path
# 1: utility name
# 2: pid: id of the observed process
# 3: interval: amount of time in milliseconds between reports
# 4: count: number of generated reports
def main( argc, argv ):
    if ( argc < 5 ):
        print( "not enough parameters passed", file=sys.stderr )
    else:
        module_name = argv[ 1 ]
        module = __import__( module_name, fromlist=[ "report" ] )
        report = module.report
        params = argv[ 2: ]
        pid, interval, count = list( map( int, params ) )
        interval = float( interval ) / 1000
        print( f'pid={pid}', f'interval={interval}', f'count={count}', file=sys.stderr )

        # make a report count times with interval seconds
        while ( count > 0 ):
            report( pid )
            count -= 1
            time.sleep( interval )

if __name__ == '__main__':
    main( len( sys.argv ), sys.argv )