# Why a new malloc trace is needed

The old malloc trace implementation depended on a glibc feature called malloc hooks. This feature was deprecated and is now removed from glibc versions >= 2.34. See this [Red Hat](https://developers.redhat.com/articles/2021/08/25/securing-malloc-glibc-why-malloc-hooks-had-go) blog for the reasoning behind the decision.

In order to keep providing a malloc trace, a new implementation was built. It uses a preloaded library, which intercepts all malloc related system calls from the C library.

The new implementation has the following benefits:

* support for Alpine linux and MacOSX in addition to glibc based linux systems
* the option to track the deallocation of memory, to get the 'live' memory
* the option to track only a fraction of the allocation calls to reduce overhead (both memory and CPU time)

# How to enable the trace
The trace needs a library called `libmallochooks` to be preloaded at the start of the VM. This is usually done by the VM itself via the `-XX:+UseMallocHooks` flag. There are scenarios when this doesn't work. For example when the VM is not launched via `java`, but loading `libjvm.so` in a launcher. In this case the launcher has to be started with the following environment variable set:
* For Linux: `LD_PRELOAD=<path-to-vm>/lib/libmallochooks.so`
* For MacOSX: `DYLD_INSERT_LIBRARIES=<path-to-vm>/lib/libmallochooks.dylib`

A VM started with `-XX:+UseMallocHooks` can then be instructed to start a malloc trace with the `jcmd <pid> MallocTrace.enable`. This command support several options:
* `-stack-depth`: This is the maximum stack length to store when tracking an allocation. 
* `-use-backtrace`: If this flag is supplied, the stack walking is done via the `backtrace` method of the glibc, if available. On MacOSX and Alpine linux the VM tries to load `libunwind` instead, for the same functionality. If neither could be found, the fallback build-in method to walk the stack is used. Using the fallback is usually faster, but might lead to stack traces with less accurate information.
* `-only-nth`: If given, not every allocation is tracked. For example `-only-nth=3` would lead to only every third allocation to be tracked. This leads to a smaller memory footprint and performance overhead. Note that the sampling is done somewhat randomly.
* `-force`: Normally the enable command fails if the trace is already enabled. Using `-force` disables and the enables the trace in this case.
* `-track-free`: If given, not only the allocation calls like `malloc` or `calloc` are tracked, but freeing the memory is tracked too. This means the result contains on the memory allocation still used. Note that this features consumes significantly more memory.
* `-detailed-stats`: If given some internal statistics about the memory use and performance overhead of the trace is sampled and can later be retrieved via the `MallocTrace.dump` command. Note that this decreases the performance of the trace slightly.

# How to get the results

To get the collected statistics the `jcmd <pid> MallocTrace.dump` command is used. This command support several options:
* `-dump-file`: This instructs the VM to send the output not the the jcmd, but write it to the given file instead. The special filenames `stdout` and `stderr` can be used to dump the output the the std output or error streams of the tracked VM. A side effect of using this option is, that the dump itself uses less memory, since the output has not to be cached by the VM.
* `-filter`: This instructs the dump command to only include stack traces which contain a function, which contains the given filter string. 
* `max-entries`: This sets the number of stacks to include in the dump. The default is 10.
* `-percentage`: If given, the dump dump all stacks, until the given percentage of the total allocation size is reached. If the `-sort-by-count` option is set, the percentage is now related to the allocation count.
* `-sort-by-count`: If given, the output is not sorted by allocation size, but by allocation count instead.
* `-internal-stats`: If given, some internal statistics are included at the end of the dump. This includes information like the memory used.

As an alternative to using `jcmd`, the trace can be enabled via [VM Flags](New-Malloc-Trace-VM-Options) too.
