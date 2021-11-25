# cifostoolbox

## Requirements

### Linux Utilities
+ `ps, pidstat`
+ `iotop`
+ `netstat`
+ `lsof`
+ `FlameGraph`
+ `perf`

### Python Libraries
+ `pipe`
+ `matplotlib`
+ `os, sys, time`

## Basic usage

`./cifrec [tool_name] [process name] [report period:ms] [number of iterations]`

### usage for plotting

`./cifrec [tool_name] [process name] [report period:ms] [number of iterations] | ./[tool_name]plotter.py`

## Featured tools

+ `fdstat` -- shows the opened files through the time
+ `nlwpstat` -- shows the number of threads opened by process through the time
+ `nlwpstater` -- shows the states of threads
+ `netstat` -- shows the statistics of ip, tcp, udp protocols
+ `iostat` -- shows the files opened by all threads of the process
+ `pidstat` -- shows the cpu % load of the process

## TODOs

+ there is nothing to do
