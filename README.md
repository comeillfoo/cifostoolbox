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
+ `nlwpstat` -- shows the states of threads

## TODOs

+ add statistics from `/proc/[pid]/io`
