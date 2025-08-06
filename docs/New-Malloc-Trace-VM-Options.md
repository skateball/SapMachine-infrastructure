Whenever you seee `<time-spec>` in an option you have to use the 's' unit for seconds, 'm' for minutes, 'h' for hours and 'd' for days. Note that you can only use one unit. E.g. `20s` or `2h`.

## Flags related to malloc tracking
* `-XX:+MallocTraceAtStartup`: Enables the memory tracking at the start of the VM. Note that even with this flags some allocations will be done earlier and not be tracked.
* `-XX:-MallocTraceExitIfFail`: When enabling the malloc trace at startup fails, the VM is stopped by default. With this flag that failure is silently ignored.
* `-XX:-MallocTraceTrackFree`: By default when the memory trace is enabled via `-XX:+MallocTraceAtStartup`, the free() calls are tracked too. If this is not the intended behavior, use this flag.
* `-XX:MallocTraceEnableDelay=<time-spec>`: This delays the startup of the memory tracking to be delayed by the given time. This can be useful to ignore all the memory allocation done during the initialization phase of the VM.
* `-XX:MallocTraceStackDepth=<stack-depth>`: Sets the maxim depth of stored stacks to `<stack-depth>`.
* `-XX:MallocTraceOnlyNth=<nth>`: If `<nth>` is not 1, then only about every `<nth>` allocation is tracked by the malloc trace. This saves memory and reduces the overhead of the trace.
* `-XX:-MallocTraceUseBacktrace`: By default the trace tries to use the `backtrace()` call of the libc or `librewind` to get the stack traces. These methods generally get better stack traces, especially with optimized code on the stack (since it might have omitted the frame pointer). If this flag is given, be use the backup method. This method is faster, but might not be able to walk the whole stack.
* `-XX:MallocTraceUnwindLibName=<name>`: The name of the `libunwind` library to use. The default should usually be OK, but if it is not found and you know where it could be found, this option allows you to specify the absolute path.
* `-XX:+MallocTraceDetailedStats`: If given, we collect more detailed statistics for the malloc trace itself. This costs some performance.

## Flags related to automatic dump of the malloc trace results.
* `-XX:+MallocTraceDumpOnError`: If given and the VM detects and out of native memory error, we dump the result of the active malloc trace. Note that a ``lot of native OOMs are not detected by the VM, so you would not get a dump.
* `-XX:MallocTraceRainyDayFund=<size>`: In order to have enough memory for the emergency dump of `-XX:+MallocTraceDumpOnError`, the VM reserves a rainy day fund at startup to be used during the dump. This option allows you to specify the size of that memory. The default is 1 MB.
* `-XX:MallocTraceDumpCount=<count>`: The number of automatic dumps of the malloc trace to be initiated by the VM. The default is 0.
* `-XX:MallocTraceDumpDelay=<time-spec>`: If `-XX:MallocTraceDumpCount` is > 0, this specifies the time interval after which the first dump is produced. The default is one hour.
* `-XX:MallocTraceDumpInterval=<time-spec>`: If `-XX:MallocTraceDumpCount` is > 0, this specifies the time interval between subsequent dumps. The default is one hour.
* `-XX:MallocTraceDumpMaxEntries=<max-entries>`: Sets the maximum amount of stacks to include in the dump output.
* `-XX:MallocTraceDumpPercentage=<percentage>`: If > 0, this ensures that the dump contains as many stacks to cover at least `<percentage>` of the total allocation size (or allocation count if `-XX::+MallocTraceDumpSortByCount` is specified too).
* `-XX::+MallocTraceDumpSortByCount`: If given, the dump output is sorted by allocation count instead of allocation size.
* `-XX:MallocTraceDumpFilter=<string-to-match>`: If given only stacks which contain the given string in a function name will be included in the dump output.
* `-XX:+MallocTraceDumpInternalStats`: if given, additional stats are included in the dump.
* `-XX:MallocTraceDumpOutput=<file|stdout|stderr>`: If given the dump output is written to the given file. Use' stderr' and 'stdout' to write to stderr and stdout respectively. The default is 'stderr'.
