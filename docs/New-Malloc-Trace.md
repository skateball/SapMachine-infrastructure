# Quickstart Guide

The [old, Linux only malloc trace](SapMachine-MallocTracer) will be [discontinued](New-Malloc-Trace-Details). The new malloc trace allows to track all native memory allocations in the JVM process on **Linux** and **MacOSX**. To be able to use the trace, the VM has to be started with the `-XX:+UseMallocHooks` flag. Then the malloc trace can be enabled via the following `jcmd` (`<pid>` is the process id of the VM process):

`jcmd <pid> MallocTrace.enable`

Now every call to `malloc`, `calloc` and so on is intercepted and a stack trace is taken. To view current statistic about the tracked allocations, the following `jcmd` can be used:

`jcmd <pid> MallocTrace.dump`

This returns the 10 stacks with the biggest total allocation size. To get more than the top 10 stacks, the '-max-entries' option can be used:

`jcmd <pid> MallocTrace.dump -max-entries=50`

The malloc trace can be disabled via:

`jcmd <pid> MallocTrace.disable`

If you only want to see the memory currently still in use, you must enable the malloc trace with the `-track-free` flag. Note that this uses more additional memory and costs some additional performance.

To get a list of all the jcmd options supported by the VM use

`jcmd <pid> help MallocTrace.enable`.

`jcmd <pid> help MallocTrace.dump`.

For more information see [this page](New-Malloc-Trace-Details).
