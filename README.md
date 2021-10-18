# cifostoolbox

## Requirements

+ `ps, pidstat`
+ `iotop`
+ `netstat`
+ `lsof`
+ `FlameGraph`
+ `perf`

## Basic launch

`./main [tool_name] [report period:ms] [number of iterations]`

## Featured tools

+ `fdstat` -- shows the opened files through the time
+ `nlwpstat` -- shows the number of threads opened by process through the time
+ `nlwpstater` -- shows the states of threads
+ `netstat` -- shows the statistics of ip, tcp, udp protocols
+ `iostat` -- shows the files opened by all threads of the process
+ `pidstat` -- shows the cpu % load of the process

## TODOs

+ add statistics from `/proc/[pid]/io`
