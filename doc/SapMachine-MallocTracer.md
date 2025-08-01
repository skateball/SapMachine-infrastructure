The SapMachine MallocTracer facility is a highly specific tool for a single task: to find hot `malloc(3)` sites for allocations happening outside the hotspot VM.

MallocTracer works for the whole process, for every `malloc(3)` call, regardless of where within the code malloc happens. So it works for mallocs from the JDK (which usually does not show up in NMT), third-party JNI libraries, or even system libraries.

It only works on Linux, and not on Alpine (it requires a glibc).

*Update 2022-08-01*: This facility relies on glibc malloc hooks, which have been removed from glibc with version 2.34. That affects modern Linux distros (e.g. Ubuntu 22.04).

## When to use it

If you have analyzed memory consumption in the JVM:
- see RSS growing
- The [*SapMachine Vitals*](https://github.com/SAP/SapMachine/wiki/SapMachine-Vitals) show C-heap memory growth: a growing delta between columns `cheap-usd` and `cheap-fre`
- But [*NMT*](https://docs.oracle.com/javase/8/docs/technotes/guides/troubleshoot/tooldescr007.html) shows nothing

Then you have determined a possible leak in C-heap happening outside of the hotspot VM itself (since NMT covers the hotspot VM). That could mean a leak in JNI/JVMTI user code, JNI JDK code, or system libraries.

## How to use it

MallocTracer can be enabled with jcmd at any point in time. The VM does not need to be restarted.

Enable MallocTracer: 

`jcmd <pid> System.malloctrace on`

Disable MallocTracer: 

`jcmd <pid> System.malloctrace off`

Print MallocTracer report: 

`jcmd <pid> System.malloctrace print`

The MallocTracer report will show malloc call sites captured when the tracer was active, ordered by invocation count ("hotness"):

```
thomas@starfish:~$ jcmd Simple System.malloctrace print
186515:
---- 0 ----
Invocs: 141312 (+141312)
Alloc Size Range: 0 - 31
[0x00007ff0beed48d0] sap::my_malloc_hook(unsigned long, void const*)+176 in libjvm.so
[0x00007ff0bfd66288] leak_malloc+47 in bwbrdg.so
[0x00007ff0bfd662b8] leakleak+18 in bwbrdg.so
[0x00007ff0bfd662cd] and_leak_like_you_dont_care+18 in bwbrdg.so
[0x00007ff0bfd662e2] throw_your_hands_in_the_air+18 in bwbrdg.so
[0x00007ff0bfd662ff] leaky_thread+26 in bwbrdg.so
---- 1 ----
Invocs: 7890 (+7890)
Alloc Size Range: 472 - 32816
[0x00007ff0beed48d0] sap::my_malloc_hook(unsigned long, void const*)+176 in libjvm.so
---- 2 ----
Invocs: 7666 (+7666)
Alloc Size: 472
[0x00007ff0beed48d0] sap::my_malloc_hook(unsigned long, void const*)+176 in libjvm.so
[0x00007ff0bf98792e] fopen+30 in libc.so.6
---- 3 ----
Invocs: 14 (+14)
Alloc Size: 65536
[0x00007ff0beed48d0] sap::my_malloc_hook(unsigned long, void const*)+176 in libjvm.so
[0x00007ff0bf282e35] sapmachine_vitals::sample_platform_values(sapmachine_vitals::Sample*)+53 in libjvm.so
[0x00007ff0bf280432] sapmachine_vitals::SamplerThread::run()+162 in libjvm.so
[0x00007ff0bf2061bb] Thread::call_run()+187 in libjvm.so
[0x00007ff0befa3911] thread_native_entry(Thread*)+225 in libjvm.so

Table size: 8171, num_entries: 7, used slots: 0, longest chain: 1, invocs: 156885, lost: 0, collisions: 0
Malloc trace off.

156885 captures (0 without stack).
```

## Notes

It is not necessary to disable the trace before getting a report.

Subsequent runs (`jcmd <pid> System.malloctrace on` followed by `jcmd <pid> System.malloctrace off`) will not reset the statistics.

MallocTracer is very lightweight but will still cost some performance and memory; don't enable it for longer periods.

## Caveats

MallocTracer is a very simple tool. It only counts how often `malloc(3)` was called, and who called it. It does not account for the amount of memory allocated.

That may cause false positives: for example, a hot `malloc(3)` site may be immediately followed by `free(3)` and therefore be completely benign. As a result, its results can be misleading; the tool should be used with caution.

In short, MallocTracer is a good tool to try before starting with more heavy-weight, complex alternatives like Valgrind.


