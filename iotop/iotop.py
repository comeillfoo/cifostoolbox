#!/usr/bin/python3
import os
import sys
import time
import subprocess as sp
import matplotlib.pyplot as plt
import math
from datetime import datetime 

def is_running( pid ):
    return os.path.exists(f"/proc/{pid}")

def list_threads( pid ):
    if ( is_running( pid ) ):
        return list( map( lambda tid: int( tid ),
        	sp.run( ["ls", f'/proc/{pid}/task'] , check=True, stdout=sp.PIPE ).stdout.decode( 'UTF-8' ).splitlines())) 
    else:
        return []

def load_io (pid, count):
	cmd = f'sudo iotop -b -p {pid} -n {count}| grep -Eo "%\s+[0-9]+\.[0-9]+" | grep -Eo "[0-9]+\.[0-9]+"'
	io_load = sp.Popen(cmd, shell=True, stdout=sp.PIPE,stderr=sp.STDOUT)
	return list(map( lambda load: float(load), io_load.communicate()[0].decode('UTF-8').splitlines()))


def load_threads (pid, count):
	
	if is_running( pid ):

		print( pid, ": running")
		tids = list_threads( pid )

		print( "tasks:", ", ".join( map( lambda tid: str( tid ), tids ) ) )

		shit_dict = {}
		tasks=[]

		for tid in tids:
			p = load_io(tid, count)
			if p:
				shit_dict[tid] = p
				tasks.append(tid)	

		return tasks, shit_dict, count
	else:
		print( pid, ": closed", file = sys.stderr)
		exit( 0 )

def iotop(tasks, penis, count):
	x=[]
	for i in range(0,count):
		x.append(i+1)

	for i in range(len(tasks)):

		plt.plot(x, penis[tasks[i]], label=str(tasks[i]))


	plt.xlabel("t")
	plt.ylabel("%")
	plt.title("IO % avg per proc")

	plt.legend()

	plt.show()
	print(penis)

def main( argc, argv ):
	if argc < 3:
		print( "not enough parameters passed", file=sys.stderr )
	else:
		iotop( *load_threads( argv[ 1 ], int( argv[ 2 ] ) ) )

if __name__ == '__main__':
	main( len( sys.argv ), sys.argv )