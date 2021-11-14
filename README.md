# cifostoolbox

## Requirements

+ `ps, pidstat`
+ `iotop`
+ `netstat`
+ `lsof`
+ `FlameGraph`
+ `perf`

## About our lord and saviour -- getpid

`getpid` is the script for defining the process id by its name

__DEPRECATED:__ Usage: `./getpid [process_name]`; __USE `pidof -s` instead__

## Basic usage

`./main [tool_name] [process name] [report period:ms] [number of iterations]`

### usage for plotting

`./main [tool_name] [process name] [report period:ms] [number of iterations] | ./[tool_name]plotter.py`

## Featured tools

+ `fdstat` -- shows the opened files through the time
+ `nlwpstat` -- shows the number of threads opened by process through the time
+ `nlwpstater` -- shows the states of threads
+ `netstat` -- shows the statistics of ip, tcp, udp protocols
+ `iostat` -- shows the files opened by all threads of the process
+ `pidstat` -- shows the cpu % load of the process

## TODOs

+ add statistics from `/proc/[pid]/io`
