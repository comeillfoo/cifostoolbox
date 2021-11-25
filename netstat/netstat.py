#!/usr/bin/python3
import matplotlib.pyplot as plt
import sys
import time
from lss import is_running
from pipe import select


# 0: file script path
# 1: protocol name
# 2: pid: id of the observed process
# 3: interval: amount of time in milliseconds between reports
# 4: count: number of generated reports
def main( argc, argv ):
    if ( argc < 5 ):
        print( "not enough parameters passed", file=sys.stderr )
    else:

        protocol = argv[ 1 ]
        try: 
            module = __import__( protocol + 'stat', fromlist=[ "stat", "script", "parameters"  ] )
        except ModuleNotFoundError:
            print( "protocol:", protocol, "not found", file=sys.stderr )
            exit( 1 )

        stat = module.stat
        script = module.script
        parameters = module.parameters

        params = argv[ 2: ]
        pid, interval, count = list( params | select( int ) )
        interval = float( interval ) / 1000
        print( f'pid={pid}', f'interval={interval}', f'count={count}', file=sys.stderr )


        # define main files snapshotting function
        def report( pid, fs, fs_keys, fs_key_size ):
            # is the main process running
            pisrun = is_running( pid )

            print( pid, ":", ( "running" if pisrun else "closed" ), file=sys.stderr )

            if pisrun:
                rudpdata = stat( pid ).decode( "UTF-8" )
                udpdata = script( rudpdata )
                for idx in range( fs_key_size ):
                    fs[ fs_keys[ idx ] ].append( udpdata[ idx ] )
                return fs
            else:
                exit( 0 )

        fs = { param: [] for param in parameters }
        fs_keys = list( fs.keys() )
        fs_keys_size = len( fs_keys )

        def netstat_plot( data, folder ):
            xs = [ x for x in range( len( data[ parameters[ 0 ] ] ) ) ]
            for key in data.keys():
                plt.rcParams["figure.figsize"] = 16, 9
                fig = plt.figure()
                plt.title( key )
                plt.plot( xs, data[ key ], label=key )
                plt.grid()
                plt.legend()
                plt.savefig( f'{folder}/{key}.png' )

        # make a report count times with interval seconds
        while ( count > 0 ):
            report( pid, fs, fs_keys, fs_keys_size )
            count -= 1
            time.sleep( interval )
        netstat_plot( fs, protocol )


if __name__ == '__main__':
    main( len( sys.argv ), sys.argv )